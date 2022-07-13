from django.db.models import Q
from django.views.generic import ListView, DetailView

from articles.models import Article, Category


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


class CategoryView(ListView):
    """View for articles of a separate category (section)."""
    model = Article
    template_name = 'articles/read_category.html'
    context_object_name = 'category_articles'
    paginate_by = 3
    slug_url_kwarg = 'category_slug'
    category = ''

    def get_queryset(self):
        """Returns a queryset of active articles of the specified category."""
        self.category = Category.objects.get(slug=self.kwargs.get('category_slug'))
        return Article.objects.filter(Q(category=self.category), Q(is_active=True))

    def get_context_data(self, *args, **kwargs):
        """Puts the title in the context according to the selected category."""
        context = super().get_context_data(**kwargs)
        context['title'] = f'Посты категории {self.category}'
        return context


class ArticleView(DetailView):
    """View for the output of a separate article."""
    model = Article
    template_name = 'articles/read-article.html'
    slug_url_kwarg = 'article_slug'
