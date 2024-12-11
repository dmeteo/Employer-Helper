from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from transliterate import translit

from app.users.managers import CustomUserManager



class User(AbstractUser):
    username = None
    email = models.EmailField(_("Email Address"),
        unique=True,
    )
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    surname = models.CharField(max_length=30, blank=False)
    phone_number = models.CharField(max_length=12, blank=False)
    image = models.ImageField(upload_to="media/", height_field=None, width_field=None, max_length=100, null=True, blank=False)
    slug = models.CharField(default="", null=False, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        self.slug = slugify(translit(f"{self.last_name} {self.first_name} {self.surname}", 'ru', reversed=True))
        return super().save(*args, **kwargs)