from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

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


def article(request, art_slug):
    article = get_object_or_404(Article, slug=art_slug)
    list_tags = article.tags.all()
    context = {
        'article': article,
        'list_tags': list_tags,
        }
    return render(request, 'detail.html', context)


def articles_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    list_articles = Article.objects.filter(tags__in=[tag])
    list_tags = Tag.objects.all()
    context = {
        'list_articles': list_articles,
        'list_tags': list_tags,
    }
    return render(request, 'index.html', context)


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
    


