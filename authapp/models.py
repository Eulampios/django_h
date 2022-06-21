from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=True, verbose_name='Email')
    age = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Возраст')
    avatar = models.ImageField(null=True, blank=True, upload_to='users')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

