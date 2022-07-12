from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

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


class ArticleView(DetailView):
    """View for the output of a separate article."""
    model = Article
    template_name = 'articles/read-article.html'

    def get_context_data(self, *args, **kwargs):
        """Getting a specific article and passing it to the context."""
        context = super().get_context_data(**kwargs)
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        context['post'] = article
        return context
