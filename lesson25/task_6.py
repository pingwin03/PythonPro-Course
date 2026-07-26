# Zadanie 6 – API do notatek
# (challenge)
# Rozbuduj aplikację z zadania 1-3. Stwórz model Note z polami title, content (TextField) i
# created_at. Zbuduj dla niego pełne API (CRUD) używając ModelViewSet i ModelSerializer.
# Użyj Postmana do przetestowania wszystkich 5 operacji (lista, detal, tworzenie,
# aktualizacja, usuwanie).


# products_app/models.py
from django.db import models

# ... (tutaj znajduje się klasa Product z poprzednich zadań)

class Note(models.Model):
    # Tworzę pole na tytuł notatki
    title = models.CharField(max_length=200)
    
    # Tworzę pole na dłuższą treść notatki
    content = models.TextField()
    
    # Automatycznie zapisuję datę utworzenia przy dodaniu do bazy
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
    
    
    # Zapisuję zmiany w modelach
python manage.py makemigrations
# Wgrywam zmiany do bazy danych
python manage.py migrate



# products_app/serializers.py
from rest_framework import serializers
from .models import Product, Note # Pamiętam o zaimportowaniu mojego nowego modelu!

# ... (tutaj znajduje się klasa ProductSerializer)

# Tworzę serializator dla notatek
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        # Wskazuję, że ten serializator dotyczy modelu Note
        model = Note
        # Zgodnie z poleceniem uwzględniam wszystkie pola
        fields = ['id', 'title', 'content', 'created_at']
        
        
        
        
# products_app/views.py
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Note
from .serializers import ProductSerializer, NoteSerializer

# ... (tutaj znajdują się ProductViewSet oraz widoki z ciasteczkami)

# Tworzę widok dla notatek obsługujący pełen CRUD
class NoteViewSet(viewsets.ModelViewSet):
    # Pobieram wszystkie notatki z bazy i sortuję je od najnowszej
    queryset = Note.objects.all().order_by('-created_at')
    
    # Podpinam odpowiedni serializator do "tłumaczenia"
    serializer_class = NoteSerializer
    
    
    
    
# my_api_project/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products_app import views 

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
# Dodaję nową linijkę, aby zarejestrować endpoint dla notatek
router.register(r'notes', views.NoteViewSet)

# ... (reszta pliku urlpatterns bez zmian)

testy zrzuty z ekranu
