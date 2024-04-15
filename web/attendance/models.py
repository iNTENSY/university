from django.contrib.auth import get_user_model
from django.db import models



class AbstractCreatedAndUpdatedAtModel(models.Model):
    updated_at = models.DateTimeField(verbose_name="Последнее обновление", auto_now=True)
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    class Meta:
        abstract = True


class Cards(AbstractCreatedAndUpdatedAtModel):
    identify_number = models.CharField(verbose_name="Уникальный номер", max_length=150, unique=True)
    is_blocked = models.BooleanField(verbose_name="Заблокирована?", default=False)

    class Meta:
        app_label = "attendance"
        verbose_name = "Ключ-карта"
        verbose_name_plural = "Ключ-карты"

    def __str__(self) -> str:
        return self.identify_number


class Attendance(AbstractCreatedAndUpdatedAtModel):
    card = models.ForeignKey(verbose_name="Ключ-карта", to="Cards", on_delete=models.SET_NULL,
                             null=True, to_field="identify_number")

    class Meta:
        verbose_name = "Посещаемость"
        verbose_name_plural = "Посещаемости"

    def __str__(self) -> str:
        return f"{self.created_at.strftime('%Y.%m.%d %H:%M:%S')} -> {self.card.owner} прошел турникет"
