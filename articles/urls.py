from django.urls import path
from articles.views import ArticleView, CategoryView

app_name = 'articles'
urlpatterns = [
    path('categories/<slug:category_slug>/', CategoryView.as_view(), name='category_read'),
    path('<slug:article_slug>/', ArticleView.as_view(), name='article_read'),
]
