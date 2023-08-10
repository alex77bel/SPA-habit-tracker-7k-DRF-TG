from django.db import models
from django.utils import timezone

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """Привычка"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.SET_NULL,
                              verbose_name='создатель привычки',
                              **NULLABLE)
    place = models.CharField(max_length=150,
                             verbose_name='место выполнения привычки')
    time = models.TimeField(default=timezone.now,
                            verbose_name='время выполнения привычки')
    action = models.CharField(max_length=150,
                              verbose_name='действие привычки')
    is_public = models.BooleanField(default=True,
                                    verbose_name='признак публичности привычки')
    duration = models.PositiveIntegerField(default=120,
                                           verbose_name='длительность выполнения в секундах')
    is_enjoyable_habit = models.BooleanField(default=False,
                                             verbose_name='признак приятной привычки')
    enjoyable_habit = models.ForeignKey('self',
                                        on_delete=models.CASCADE,
                                        # related_name='useful_habit',
                                        verbose_name='приятная привычка',
                                        **NULLABLE)
    fee = models.CharField(max_length=150,
                           verbose_name='вознаграждение', **NULLABLE)
    periodicity = models.PositiveSmallIntegerField(verbose_name='интервал между выполнением привычек, суток',
                                                   default=1)

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ('time',)

    def __str__(self):
        return f'Действие: {self.action}, время: {self.time}, место: {self.place}, выполнить за {self.duration} секунд'

# class EnjoyableHabit(Habit):
#     """Приятная привычка"""
#
#     class Meta:
#         verbose_name = 'приятная привычка'
#         verbose_name_plural = 'приятные привычки'
#         ordering = ('time',)
#
#     def __str__(self):
#         return f'{self.action}, время: {self.time}, место: {self.place}, выполнить за {self.duration} секунд'
#
#
# class UsefulHabit(Habit):
#     """Полезная привычка"""
#     enjoyable_habit = models.ForeignKey(EnjoyableHabit,
#                                         on_delete=models.SET_NULL,
#                                         related_name='useful_habit',
#                                         verbose_name='приятная привычка',
#                                         **NULLABLE)
#     fee = models.CharField(max_length=150,
#                            verbose_name='вознаграждение', **NULLABLE)
#
#     periodicity = models.PositiveSmallIntegerField(verbose_name='периодичность выполнения привычки, раз в сутки',
#                                                    default=1)
#
#     class Meta:
#         verbose_name = 'полезная привычка'
#         verbose_name_plural = 'полезные привычки'
#         ordering = ('time',)
#
#     def __str__(self):
#         return f'Задание: {self.action}, время: {self.time}, место: {self.place}, выполнить за {self.duration} ' \
#                f'секунд (приятное действие: {self.enjoyable_habit if self.enjoyable_habit else self.fee})'
