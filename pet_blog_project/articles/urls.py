from django.urls import path
from .views import ArticleListView, ArticleDetailView, TagListView


urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('<slug:slug>', TagListView.as_view(), name='tag_list'),
]