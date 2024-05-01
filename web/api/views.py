import requests
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from university.settings import BOT_TOKEN
from users.models import Groups
from .serializers import AttendanceReadSerializer, AttendanceWriteSerializer, CardsReadSerializer, CardsWriteSerializer, \
    GroupSerializer, GroupAttendanceSerializer
from attendance.models import Attendance, Cards

Users = get_user_model()


class AttendanceViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Attendance.objects.all()
    permission_classes = (permissions.IsAdminUser,)

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return AttendanceReadSerializer
        return AttendanceWriteSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        user = Cards.objects.get(identify_number=request.data.get("card")).owner
        if user.telegram_id_notification:
            headers = {
                "chat_id": str(user.telegram_id_notification),
                "text": f"{user} прошел турникет университета"
            }
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            requests.get(url, headers=headers)
        return response


class CardsViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Cards.objects.all()
    permission_classes = (permissions.IsAdminUser,)

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return CardsReadSerializer
        return CardsWriteSerializer


class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer
    permissions = (permissions.IsAdminUser,)
    lookup_field = "title"


class GroupAttendanceViewSets(mixins.ListModelMixin,
                              GenericViewSet):
    permissions = (permissions.IsAdminUser,)

    def list(self, *args, **kwargs):
        result = Groups.attendance.make_for_group(kwargs["title"])
        if not result:
            return Response(data={"error": "Group with title not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = GroupAttendanceSerializer(data=list(result), many=True)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
