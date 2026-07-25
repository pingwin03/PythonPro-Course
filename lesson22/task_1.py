# Zadanie 1 – Normalizacja Postów (Kategorie)
# Zadania-wyzwania:
# Stwórz nowy model Category z polem name. Następnie w modelu Post dodaj pole category
# będące kluczem obcym (ForeignKey) do modelu Category. Nie zapomnij o stworzeniu i
# zaaplikowaniu migracji! (proste)


# Do - blog/models.py tworzymy category

from django.db import models

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

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    # 2. Dodajemy pole category (klucz obcy)
    # null=True pozwala, by istniejące posty w bazie początkowo nie miały kategorii
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    
    publication_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
    
    # po tym migracja
    python manage.py makemigrations
    python manage.py migrate