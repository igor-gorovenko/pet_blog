from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name
    

class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Article(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self) -> str:
        return self.title




