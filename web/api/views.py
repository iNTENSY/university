import requests
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, status, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from university.settings import BOT_TOKEN
from .serializers import AttendanceReadSerializer, AttendanceWriteSerializer, CardsReadSerializer, CardsWriteSerializer
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
            message = f"{user} прошел турникет университета"
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={user.telegram_id_notification}&text={message}"
            requests.get(url)
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
