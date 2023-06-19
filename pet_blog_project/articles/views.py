from django.shortcuts import get_object_or_404, render

from .models import Article, Tag, Author


def index(request):
    list_articles = Article.objects.all()
    list_tags = Tag.objects.all()
    list_authors = Author.objects.all()
    context = {
        'list_articles': list_articles,
        'list_tags': list_tags,
        'list_authors': list_authors,
    }
    return render(request, 'index.html', context)


def article(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'detail.html', {'article': article})