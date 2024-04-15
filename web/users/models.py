from django.contrib.auth.models import AbstractUser
from django.db import models

from attendance.models import Cards


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
