# Zadanie 9 – Relacje w API
# (challenge)
# Stwórz dwa modele: Author (name) i Book (title, publication_year oraz klucz obcy do
# Author). Stwórz serializatory i ViewSety dla obu modeli. Zmodyfikuj BookSerializer tak, aby
# przy wyświetlaniu książki pokazywał nazwę autora, a nie tylko jego ID. Wskazówka:
# poszukaj informacji o Nested Serializers lub StringRelatedField w dokumentacji DRF




# products_app/models.py
from django.db import models

# ... (poprzednie modele Product i Note zostają bez zmian)

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
    
    
    
    
    
# python manage.py makemigrations
# python manage.py migrate

# Teraz wchodzę do serializers.py. Zgodnie z podpowiedzią, użyję StringRelatedField
# products_app/serializers.py
from rest_framework import serializers
from .models import Product, Note, Author, Book # Importuję nowe modele

# ... (poprzednie serializatory zostają bez zmian)

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    # Wykorzystuję StringRelatedField, aby pobrać wartość z metody __str__ modelu Author
    # Ustawiam source='author', aby DRF wiedział, skąd wziąć dane
    author_name = serializers.StringRelatedField(source='author', read_only=True)

    class Meta:
        model = Book
        # Dodaję zarówno 'author' (do obsługi ID), jak i 'author_name' (do wyświetlania nazwy)
        fields = ['id', 'title', 'publication_year', 'author', 'author_name']
        
        
        
        



# otwieram plik views.py i dodaję ModelViewSet
# products_app/views.py
from rest_framework import viewsets
from .models import Product, Note, Author, Book
from .serializers import ProductSerializer, NoteSerializer, AuthorSerializer, BookSerializer

# ... (poprzednie widoki zostają bez zmian)

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
# my_api_project/urls.py
from rest_framework.routers import DefaultRouter
from products_app import views 

router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'notes', views.NoteViewSet)
# Rejestruję endpointy dla autorów i książek
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)

# ... (reszta pliku urlpatterns bez zmian)

# Test zrzut ekranu do zadania 9