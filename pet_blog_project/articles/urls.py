from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('article/<slug:art_slug>/', views.article, name='detail'),
    path('tag/<slug:tag_slug>/', views.articles_by_tag, name='by_tag'),
    path('author/<slug:author_slug>', views.articles_by_author, name='by_author'),
    path('date/<slug:date_slug>', views.articles_by_date, name='by_date'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]