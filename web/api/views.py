import re

import requests

from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, status, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from university.settings import BOT_TOKEN, CURRENT_EDUCATION_HALF
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
    queryset = Groups.objects.all()
    serializer_class = GroupAttendanceSerializer
    permissions = (permissions.IsAdminUser,)

    def list(self, *args, **kwargs):
        from_date, to_date = self.get_validated_date_format()
        result = Groups.attendance.make_for_group_by_title(kwargs["title"], from_date, to_date)
        if not result:
            return Response(data={"error": "Group with title not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = GroupAttendanceSerializer(data=list(result), many=True)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_validated_date_format(self):
        from_date = self.request.query_params.get("from_date")
        to_date = self.request.query_params.get("to_date")

        pattern = r'^\d{4}-\d{2}-\d{2}$'
        result_from_date = from_date if re.match(pattern, str(from_date)) else CURRENT_EDUCATION_HALF["start"]
        result_to_date = from_date if re.match(pattern, str(to_date)) else CURRENT_EDUCATION_HALF["end"]
        return result_from_date, result_to_date