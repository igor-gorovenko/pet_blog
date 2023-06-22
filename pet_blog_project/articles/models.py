from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(null=False)

    def __str__(self) -> str:
        return f'{self.name}'


class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    slug = models.SlugField(null=False)
    age = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    

class Date(models.Model):
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(null=False)

    def __str__(self) -> str:
        return f'{self.date}'


class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(null=False, db_index=True, verbose_name='URL')
    text = models.TextField()
    date = models.ForeignKey(Date, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self) -> str:
        return f'{self.title}'




