from datetime import datetime, timedelta
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):
    """The model for the category."""
    category_name = models.CharField(max_length=128)
    is_active = models.BooleanField(verbose_name="раздел активен", default=True, db_index=True)

    def __str__(self):
        """Forms a printable representation of the object.
        Returns the name of the category.
        """
        return str(self.category_name)

    class Meta:
        """Defines the model involved and the fields used in the form.
        """
        ordering = ('id',)


class HabrUser(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid4())
    user_name = models.CharField(verbose_name="логин", max_length=128, blank=False)
    first_name = models.CharField(verbose_name="имя", max_length=128, blank=False)
    last_name = models.CharField(verbose_name="фамилия", max_length=128, blank=False)
    avatar = models.ImageField(upload_to="users_avatars", blank=True)
    email = models.CharField(verbose_name="email", max_length=128, blank=False)
    age = models.PositiveIntegerField(verbose_name="возраст", default=18)
    role = models.PositiveIntegerField(verbose_name="тип пользователя", default=18)
    registration_time = models.DateTimeField(verbose_name="время регистрации", default=datetime.now())
    is_active = models.BooleanField(verbose_name="пользователь активен", default=True, db_index=True)
    activation_key = models.CharField(verbose_name="ключ подтверждения", max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(verbose_name="актуальность ключа", default=datetime.now() + timedelta(hours=48))


class Tag(models.Model):
    tag_name = models.CharField(verbose_name="наименование", max_length=128, blank=False)


class Article(models.Model):
    registration_time = models.DateTimeField(verbose_name="время создания", default=datetime.now())
    is_active = models.BooleanField(verbose_name="статья активна", default=False, db_index=True)
    title = models.CharField(verbose_name="заголовок", max_length=128, blank=False)
    body = models.CharField(verbose_name="тело", max_length=100000, blank=False)
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(HabrUser, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
