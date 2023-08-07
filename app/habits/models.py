from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    pass
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='создатель привычки',
                             **NULLABLE)
