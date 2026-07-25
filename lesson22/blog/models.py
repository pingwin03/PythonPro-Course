from django.db import models
from django.utils import timezone




# 1. Tworzymy nowy model Category
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    # 2. Dodajemy pole category (klucz obcy)
    # null=True pozwala, by istniejące posty w bazie początkowo nie miały kategorii
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    
    publication_date = models.DateTimeField()
    
    # NOWE POLE RELACYJNE
    # blank=True oznacza, że post może nie mieć żadnych tagów (nie są obowiązkowe)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

