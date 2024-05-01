from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Count, Q

from attendance.models import Cards, Attendance


class Users(AbstractUser):
    REQUIRED_FIELDS = ["first_name", "last_name"]
    middle_name = models.CharField(verbose_name="Отчество", null=True, max_length=150, blank=True)
    is_notification_enabled = models.BooleanField(verbose_name="Включены ли уведомления по телеграму?", default=False)
    telegram_id_notification = models.CharField(verbose_name="ID чата для уведомления", null=True, blank=True, max_length=50)
    card = models.OneToOneField(verbose_name="Ключ-карта", to=Cards, on_delete=models.CASCADE, related_name="owner", null=True)

    class Meta:
        app_label = "users"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}{f' {self.middle_name}' if self.middle_name else ''}".title()


class AttendanceManager(models.Manager):
    def make_for_group(self, title: str, from_date: str = None, to_date: str = None):
        try:
            group = Groups.objects.get(title=title)
        except ObjectDoesNotExist:
            return None
        statement = (
            group.students
            .annotate(
                counter=Count(
                    "card__attendance__created_at__date",
                    distinct=True,
                    filter=Q(
                        card__attendance__created_at__date__gte=from_date,
                        card__attendance__created_at__date__lte=to_date,
                    )
                )
            )
            .filter()
            .values("last_name", "first_name", "middle_name", "counter")
        )
        return statement


class Groups(models.Model):
    title = models.CharField(verbose_name="Краткое наименование группы", max_length=20, unique=True)
    curator = models.ForeignKey(verbose_name="Куратор", to=Users, on_delete=models.SET_NULL, null=True, related_name="self_groups")
    students = models.ManyToManyField(verbose_name="Студенты", to=Users, related_name="self_group", blank=True)

    objects = models.Manager()
    attendance = AttendanceManager()

    class Meta:
        app_label = "users"
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self) -> str:
        return self.title
