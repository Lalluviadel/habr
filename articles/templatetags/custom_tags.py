"""Contains custom template tags."""

from django import template
from ..models import Category
register = template.Library()


@register.inclusion_tag('articles/includes/menu.html', takes_context=True)
def show_categories(context):
    """Template tag for displaying menu sections (categories of articles from the database)."""
    return {
        "category_menu_items": Category.objects.filter(is_active=True),
    }
