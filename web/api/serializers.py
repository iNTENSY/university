from rest_framework import serializers

from attendance.models import Attendance, Cards


class AttendanceWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        exclude = ("id",)


class AttendanceReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"


class CardsWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        exclude = ("id", )


class CardsReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"
