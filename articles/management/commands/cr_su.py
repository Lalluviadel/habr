"""Contains custom commands for easy launch by manage.py."""
from userapp.models import HabrUser
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    """A command for quickly creating a superuser."""
    def handle(self, *args, **options):
        user = HabrUser.objects.create_superuser('admin', 'admin@mail.ru', '1')
        user.is_active = True
        user.save()
