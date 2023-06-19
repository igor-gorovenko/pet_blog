from django.views.generic import ListView, DetailView

from .models import Article, Author, Tag


class ArticleListView(ListView):
    model = Article
    template_name = 'index.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class TagListView(ListView):
    model = Tag
    template_name = 'index.html'