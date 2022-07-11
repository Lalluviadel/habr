"""Provides package integration into the admin panel."""
from django.contrib import admin

from articles.models import Category, HabrUser, Tag, Article

admin.site.register(Category)
admin.site.register(HabrUser)
admin.site.register(Tag)
admin.site.register(Article)
