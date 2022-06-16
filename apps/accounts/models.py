from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import AccountManager
import uuid
from django.urls import reverse


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email Address'), unique=True)
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    class Meta:
        verbose_name_plural = "accounts"
        verbose_name = "account"

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email}"


