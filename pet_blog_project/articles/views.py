from django.shortcuts import get_object_or_404, render

from .models import Article, Author


def index(request):
    list_articles = Article.objects.order_by("-creation_date")[:5]
    context = {
        'list_articles': list_articles,
    }
    return render(request, 'articles/index.html', context)


def article(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'articles/detail.html', {'article': article})


def author(page, id):
    try:
        author = Author.objects.get(pk=id)
    except Author.DoesNotExist:
        raise Http404('Author does not exist')
    return HttpResponse(request, 'authors/author', {'author': author})
