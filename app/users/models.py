from django.contrib.auth.models import AbstractUser
from django.db import models

from app.users.manager import UserManager

NULLABLE = {'blank': True, 'null': True}


def upload_path(file, model) -> str:
    return f"avatars/{model.pk}/{file}"


class CustomUser(AbstractUser):
    """Модель пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    tg_username = models.CharField(max_length=150, unique=True, verbose_name='никнейм в телеграмме')
    tg_chat_id = models.CharField(max_length=150, **NULLABLE, verbose_name='ID чата в телеграмм')
    name = models.CharField(max_length=50, verbose_name='имя', **NULLABLE)
    phone = models.CharField(max_length=50, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to=upload_path, verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    # def update_tg_chat_id(self, tg_chat_id):
    #     self.tg_chat_id = tg_chat_id
    #     self.save()

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('first_name',)
