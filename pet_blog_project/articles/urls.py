from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.article, name='detail'),
    path('tag/<slug:tag_slug>/', views.articles_by_tag, name='tag'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]