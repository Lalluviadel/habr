from django.urls import path
from articles.views import ArticleView

app_name = 'articles'
urlpatterns = [
    path('<slug:article_slug>/', ArticleView.as_view(), name='article_read'),
]
