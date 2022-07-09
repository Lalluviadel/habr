from django.views.generic import TemplateView


class MainView(TemplateView):
    """View for the main page."""
    template_name = 'articles/index.html'
