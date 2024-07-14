from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None

    nick_name = models.CharField(max_length=150, verbose_name='никнэйм')
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(**NULLABLE, verbose_name='аватарка')
    country = models.CharField(max_length=150, verbose_name='страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nick_name

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('nick_name',)
