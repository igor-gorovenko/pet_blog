from django.shortcuts import get_object_or_404, render

from .models import Article


def index(request):
    list_articles = Article.objects.all()
    context = {
        'list_articles': list_articles,
    }
    return render(request, 'index.html', context)


def article(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'detail.html', {'article': article})