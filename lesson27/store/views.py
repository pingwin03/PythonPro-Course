import time
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# --- Zadanie 3: Buforowanie całej odpowiedzi widoku ---
@cache_page(60)
@api_view(['GET'])
def product_list(request):
    """
    Widok zwracający listę wszystkich produktów.
    Cała odpowiedź jest buforowana na 60 sekund.
    """
    products = list(Product.objects.all().values())
    return Response(products)


# --- Zadanie 7: Selektywne buforowanie fragmentów danych ---
@api_view(['GET'])
def selective_cache_view(request):
    """
    Widok pokazujący użycie niskopoziomowego API cache.
    Cachuje tylko zasobożerne obliczenia, a pobieranie z bazy wykonuje zawsze na żywo.
    """
    # Proste i szybkie zapytanie do bazy danych (tego NIE cachuję)
    fast_db_data = list(Product.objects.all()[:3].values())

    # Skomplikowane i długie obliczenia (to CACHUJĘ)
    cache_key = 'my_heavy_computation'
    complex_data = cache.get(cache_key)

    if complex_data is None:
        # Symulacja długich obliczeń
        time.sleep(3)
        
        complex_data = {
            "value": 999,
            "description": "Wynik trudnego algorytmu"
        }
        
        # Zapis do cache na 60 sekund
        cache.set(cache_key, complex_data, timeout=60)
        data_source = "Wyliczono na żywo (trwało 3 sekundy)"
    else:
        data_source = "Pobrano z cache (błyskawicznie!)"

    response_data = {
        "db_data": fast_db_data,
        "complex_data": complex_data,
        "complex_data_source": data_source
    }

    return Response(response_data)


# --- Zadanie 8 i 9: ViewSet z różnymi czasami cache i inwalidacją ---
@method_decorator(cache_page(600), name='list')
class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet dla modelu Product.
    - Metoda 'list' (GET na listę) jest cachowana na 10 minut za pomocą dekoratora.
    - Metoda 'retrieve' (GET na szczegóły) jest cachowana na 1 minutę z użyciem własnego klucza.
    - Zmiany (update/patch) unieważniają cache dla widoku szczegółów tego obiektu.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        """Nadpisana metoda do ręcznego cachowania pojedynczego obiektu."""
        instance = self.get_object()
        
        # Własny klucz na podstawie ID produktu
        cache_key = f'product_detail_{instance.pk}'
        
        cached_data = cache.get(cache_key)
        
        if cached_data:
            return Response(cached_data)

        # Cache miss - generujemy dane
        serializer = self.get_serializer(instance)
        data = serializer.data
        
        # Zapis na 60 sekund
        cache.set(cache_key, data, timeout=60)
        
        return Response(data)

    def perform_update(self, serializer):
        """Nadpisana metoda zapisu aktualizacji, która czyści stary cache."""
        instance = serializer.save()
        
        # Odtworzenie klucza i usunięcie starych danych z cache
        cache_key = f'product_detail_{instance.pk}'
        cache.delete(cache_key)