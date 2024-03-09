from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    first_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='first name')
    last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='last name')
    telegram_id = models.CharField(max_length=100, blank=True, null=True, verbose_name='telegram_id')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
