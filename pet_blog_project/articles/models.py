from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=120)
    article_text = models.TextField()
    creation_date = models.DateField()


class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.SmallIntegerField()

