from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta

class HabrUser(AbstractUser):
    """The model for the user."""
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(verbose_name="логин", max_length=128, blank=False, unique=True)
    first_name = models.CharField(verbose_name="имя", max_length=128, blank=False)
    last_name = models.CharField(verbose_name="фамилия", max_length=128, blank=False)
    avatar = models.ImageField(upload_to="users_avatars", blank=True)
    email = models.CharField(verbose_name="email", max_length=128, unique=True, blank=False)
    age = models.PositiveIntegerField(verbose_name="возраст", default=18)
    registration_time = models.DateTimeField(verbose_name="время регистрации", default=datetime.now)
    is_active = models.BooleanField(verbose_name="пользователь активен", default=True, db_index=True)
    activation_key = models.CharField(verbose_name="ключ подтверждения", max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(verbose_name="актуальность ключа",
                                                  default=datetime.now() + timedelta(hours=48))
    banned_until = models.DateTimeField(verbose_name="забанен до", blank=True, null=True)

    def __str__(self):
        """Forms a printable representation of the object.
        Returns the username of the user.
        """
        return str(self.username)

    class Meta:
        """Ordering users according to their id.
        """
        ordering = ('uuid',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
