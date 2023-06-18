from django.contrib import admin

from .models import Article, Author, Tag

admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Article)


