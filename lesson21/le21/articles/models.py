from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    # Dodajemy klucz obcy do modelu Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    # Nowe pola do Zadania 8:
    is_published = models.BooleanField(default=True)
    # auto_now_add=True automatycznie zapisze datę przy tworzeniu artykułu
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title