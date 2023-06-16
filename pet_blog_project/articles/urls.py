from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/article/', views.article, name='article'),
    path('<int:id>/author/', views.author, name='author'),
]