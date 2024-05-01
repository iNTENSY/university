from rest_framework import serializers

from attendance.models import Attendance, Cards
from users.models import Groups


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


class CurrentGroupReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = "__all__"


class GroupAttendanceSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    middle_name = serializers.CharField()
    counter = serializers.IntegerField()
