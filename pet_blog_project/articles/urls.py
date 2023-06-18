from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:id>/', views.article, name='article'),
    path('author/<int:id>/', views.author, name='author'),
    path('tag/<slug:tag_slug>', views.article_by_tag, name='tag'),
]