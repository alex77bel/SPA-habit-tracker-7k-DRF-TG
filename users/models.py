from django.contrib.auth.models import AbstractUser
from django.db import models

from users.manager import UserManager

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Модель пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    tg_username = models.CharField(max_length=150, verbose_name='никнейм в телеграмме', **NULLABLE)
    tg_chat_id = models.CharField(max_length=150, verbose_name='ID чата в телеграмм', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('email',)
