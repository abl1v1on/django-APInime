from django.db import models

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Необходимо указать адрес электронной почты')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField('email', unique=True)
    is_subscribed = models.BooleanField(default=False, verbose_name='Подписка на рассылку')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self) -> str:
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile_user', on_delete=models.CASCADE, verbose_name='Пользователь')
    profile_pic = models.ImageField('Аватарка', upload_to='profile_pics/%Y/%m', blank=True)
    desc = models.TextField('Описание', max_length=1000, blank=True)

    def __str__(self) -> str:
        return self.user.email
    