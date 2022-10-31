from django.db import models


class Author(models.Model):
    name=models.CharField(max_length=10)
    address = models.CharField(max_length=12)
    email=models.EmailField()

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title=models.CharField(max_length=20)
    book_author = models.ForeignKey(Author,on_delete = models.CASCADE)
    no_pages = models.IntegerField()

    def __str__(self):
        return self.title
# Create your models here.
