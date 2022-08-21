from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import AccountManager


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Email Address', unique=True)
    first_name = models.CharField('First Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    class Meta:
        verbose_name_plural = "accounts"
        verbose_name = "account"

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email}"


