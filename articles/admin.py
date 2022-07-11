"""Provides package integration into the admin panel."""
from django.contrib import admin

from articles.models import Category

admin.site.register(Category)
