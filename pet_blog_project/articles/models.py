import datetime
from django.utils import timezone
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=120)
    article_text = models.TextField()
    creation_date = models.DateField()

    def __str__(self) -> str:
        return self.title
    
    def was_created_recently(self):
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1) 


class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.SmallIntegerField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

