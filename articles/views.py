from django.views.generic import ListView

from articles.models import Article


class MainView(ListView):
    """View for the main page."""
    model = Article
    template_name = 'articles/index.html'
    context_object_name = 'all_articles'
    paginate_by = 3

    def get_queryset(self):
        """Displaying all active articles.
         Articles are displayed in an orderly manner, starting from the most recent."""
        return Article.objects.filter(is_active=True)
