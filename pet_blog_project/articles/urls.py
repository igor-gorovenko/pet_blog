from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:id>/', views.article, name='article'),
    path('author/<int:id>/', views.author, name='author'),
]