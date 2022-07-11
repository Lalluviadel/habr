from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=128)
    is_active = models.BooleanField()
