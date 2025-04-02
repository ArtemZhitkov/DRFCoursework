from django.db import models

from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    place = models.CharField(
        max_length=100,
        verbose_name="Место",
        help_text="Укажите действие, которое представляет собой привычка",
    )
    time = models.TimeField(
        verbose_name="Время",
        help_text="Установите время, когда необходимо выполнять привычку",
    )
    action = models.CharField(
        max_length=120,
        verbose_name="Действие",
        help_text="Укажите действие, которое представляет собой привычка",
    )
    pleasant_habit = models.BooleanField(
        default=True,
        verbose_name="Признак приятной привычки",
        help_text="Привычка, которую можно привязать к выполнению полезной привычки",
    )
    related_habit = models.ForeignKey(
        "self", on_delete=models.CASCADE, verbose_name="Связанная привычка"
    )
    periodicity = models.PositiveSmallIntegerField(
        default=1,
        verbose_name="Периодичность",
        help_text="Периодичность выполнения привычки для напоминания в днях.(по умолчанию ежедневная)",
    )
    reward = models.CharField(
        max_length=100,
        verbose_name="Вознаграждение",
        help_text="Чем пользователь должен себя вознаградить после выполнения",
    )
    time_to_complete = models.TimeField(verbose_name="Время на выполнение")
    is_published = models.BooleanField(default=True, verbose_name="Признак публичности")
