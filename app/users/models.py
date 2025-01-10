from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from transliterate import translit

from app.users.managers import CustomUserManager


class Role(models.Model):
    name = models.CharField(max_length=30)
    level = models.SmallIntegerField(verbose_name="Уровень роли")

    class Meta:
        db_table = 'roles'
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


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
    role = models.ForeignKey(Role, 
                             on_delete=models.CASCADE,
                             null=True)
    manager = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="subordinates",  # получить всех стажеров
        verbose_name="Руководитель"
    )

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
        base_slug = slugify(translit(f"{self.last_name} {self.first_name} {self.surname}", 'ru', reversed=True))
        slug_candidate = base_slug
        counter = 1

        while User.objects.filter(slug=slug_candidate).exclude(pk=self.pk).exists():
            slug_candidate = f"{base_slug}-{counter}"
            counter += 1

        self.slug = slug_candidate
        super().save(*args, **kwargs)