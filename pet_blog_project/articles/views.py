from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy

from .models import Article, Author, Tag


def index(request):
    list_articles = Article.objects.all()
    list_authors = Author.objects.all()
    list_tags = Tag.objects.all()
    
    context = {
        'list_articles': list_articles,
        'list_authors': list_authors,
        'list_tags': list_tags,
    }
    return render(request, 'index.html', context)


def article(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'detail.html', {'article': article})


def author(request, id):
    author = get_object_or_404(Author, pk=id)
    return render(request, 'author.html', {'author': author})
