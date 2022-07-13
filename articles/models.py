"""
Stores the user, article, category and tag models.
"""

from datetime import datetime
from django.db import models
from userapp.models import HabrUser

class Category(models.Model):
    """The model for the category."""
    category_name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    is_active = models.BooleanField(verbose_name="раздел активен", default=True, db_index=True)

    def __str__(self):
        """Forms a printable representation of the object.
        Returns the name of the category.
        """
        return str(self.category_name)

    class Meta:
        """Ordering categories according to their id.
        """
        ordering = ('id',)
        verbose_name = 'Раздел сайта'
        verbose_name_plural = 'Разделы сайта'




class Tag(models.Model):
    """The model for the tag."""
    tag_name = models.CharField(verbose_name="наименование", max_length=128, blank=False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        """Forms a printable representation of the object.
        Returns the name of the tag.
        """
        return str(self.tag_name)

    class Meta:
        """Ordering users according to their id.
        """
        ordering = ('tag_name',)
        verbose_name = 'Теги'
        verbose_name_plural = 'Тег'


class Article(models.Model):
    """The model for the article."""
    registration_time = models.DateTimeField(verbose_name="время создания", default=datetime.now)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    is_active = models.BooleanField(verbose_name="статья активна", default=False, db_index=True)
    title = models.CharField(verbose_name="заголовок", max_length=128, blank=False)
    body = models.CharField(verbose_name="тело", max_length=100000, blank=False)
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(HabrUser, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        """Forms a printable representation of the object.
        Returns the title of the article.
        """
        return str(self.title)

    class Meta:
        """Ordering articles according to their date of addition (the most recent ones first).
        """
        ordering = ['-registration_time', ]
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
