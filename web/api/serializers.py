from rest_framework import serializers

from attendance.models import Attendance


class AttendanceWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        exclude = ("id",)


class AttendanceReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"
