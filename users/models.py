from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    username = None

    nick_name = models.CharField(max_length=150, verbose_name='никнэйм')
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(**NULLABLE, verbose_name='аватарка', upload_to='users/avatars')
    country = models.CharField(max_length=150, verbose_name='страна')

    token = models.CharField(max_length=100, verbose_name='токен', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nick_name

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('nick_name',)
