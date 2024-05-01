from django.contrib import admin

from users.models import Groups
from .models import Cards, Attendance


@admin.register(Cards)
class CardsAdmin(admin.ModelAdmin):
    pass


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    pass


@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    pass
