"""Provides package integration into the admin panel."""
from django.contrib import admin

from articles.models import Category, Tag, Article


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'slug', 'is_active')
    list_display_links = ('id', 'category_name')
    search_fields = ('title', 'is_active')
    prepopulated_fields = {'slug': ('category_name',)}


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'registration_time', 'user', 'category')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'is_active')
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name')
    list_display_links = ('id', 'tag_name',)
    search_fields = ('tag_name',)
    prepopulated_fields = {'slug': ('tag_name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)

admin.site.register(Tag, TagAdmin)
