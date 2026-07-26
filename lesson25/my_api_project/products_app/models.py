
from django.db import models

class Product(models.Model):
    # Tworzę pole na nazwę produktu (wymaga określenia max_length)
    name = models.CharField(max_length=255)
    
    # Tworzę pole na cenę produktu (wymaga określenia max_digits i decimal_places)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Dodaję metodę __str__, aby mój obiekt ładnie wyświetlał się w panelu admina
    def __str__(self):
        return self.name
    
    
class Note(models.Model):
    # Tworzę pole na tytuł notatki
    title = models.CharField(max_length=200)
    
    # Tworzę pole na dłuższą treść notatki
    content = models.TextField()
    
    # Automatycznie zapisuję datę utworzenia przy dodaniu do bazy
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    
    
    
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        # Ta metoda jest kluczowa dla StringRelatedField, o którym mowa w zadaniu!
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    # Tworzę klucz obcy łączący książkę z modelem Author
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title