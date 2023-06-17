import datetime
from django.urls import reverse
from django.utils import timezone
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Tag(models.Model):
    name = models.CharField(max_length=40, help_text='Enter a tag')

    def __str__(self) -> str:
        return self.name
    

class Article(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, help_text='Select a tag')

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])
    
    def was_created_recently(self):
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1) 


