# Zadanie 8 – Różne czasy cache dla różnych metod ViewSetu
# Stwórz ModelViewSet dla jednego z Twoich modeli. Użyj dekoratora
# @method_decorator(cache_page(...)) tak, aby widok listy (list) był cachowany na 10 minut,
# a widok szczegółów (retrieve) tylko na 1 minutę. Metody create, update, destroy nie
# powinny być cachowane w ogóle.


# Przygotowanie Serializera

# store/serializers.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
        
# Implementacja ModelViewSet w store/views.py    


# store/views.py (dodaję do istniejącego pliku)

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

# 60 * 10 = 600 sekund (10 minut)
# 60 * 1 = 60 sekund (1 minuta)

@method_decorator(cache_page(600), name='list')
@method_decorator(cache_page(60), name='retrieve')
class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet dla modelu Product.
    - Metoda 'list' (np. GET /api/products/) będzie w cache przez 10 minut.
    - Metoda 'retrieve' (np. GET /api/products/1/) będzie w cache przez 1 minutę.
    - Metody 'create', 'update', 'destroy' (POST, PUT, PATCH, DELETE) nie są cachowane.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    
    
    
# Podpięcie ViewSetu do cache_project/urls.py

# cache_project/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store.views import product_list, selective_cache_view, ProductViewSet

# Konfiguruję router dla mojego ViewSetu
router = DefaultRouter()
router.register(r'api/products', ProductViewSet, basename='api-product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    
    # Moje poprzednie widoki funkcyjne
    path('products/', product_list, name='product-list'),
    path('selective/', selective_cache_view, name='selective-cache'),
    
    # Podpinam wszystkie ścieżki wygenerowane przez router (w tym list, retrieve, create itp.)
    path('', include(router.urls)),
]

# Testowanie
# 1. Wchodzę pod adres [http://127.0.0.1:8000/api/products/]
# (metoda list). Wynik ładuje się z bazy, zapisuje do cache i przez kolejne 10 minut 
# każde odświeżenie (lub żądanie GET od innych użytkowników)
# będzie serwowane błyskawicznie z pliku, omijając bazę danych.

# 2. Wchodzę pod adres konkretnego produktu,
# [http://127.0.0.1:8000/api/products/1/]
# (metoda retrieve). Wynik jest serwowany z cache, ale traci ważność już po 1 minucie.