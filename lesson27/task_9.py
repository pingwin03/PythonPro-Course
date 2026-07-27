# Zadanie 9 – Unieważnianie cache po aktualizacji obiektu
# Rozszerz zadanie 8. Zaimplementuj logikę, która po każdej udanej operacji update lub
# partial_update na obiekcie, unieważni (usunie) klucz cache dla widoku szczegółów
# (retrieve) tego konkretnego obiektu. Wskazówka: sygnały Django (post_save) lub
# nadpisanie metody perform_update w ViewSetcie mogą być pomocne. Musisz też wiedzieć,
# jak Django buduje klucze cache dla widoków (może to wymagać trochę researchu lub
# użycia własnych kluczy)




# Idąc za drugą częścią wskazówki ("lub użycia własnych kluczy"),
# zdecydowałem się na najczystsze i najczęściej stosowane 
# podejście w Django REST Framework



# 1. Zdejmuję dekorator @cache_page z metody retrieve.

# 2. Nadpisuję metodę retrieve, używając niskopoziomowego API,
# co pozwala mi nadać mój własny, prosty klucz (np. product_detail_1).

# 3. Nadpisuję metodę perform_update, aby po udanym zapisie do bazy usunęła ten konkretny klucz z cache.

# store/views.py

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache # Importuję niskopoziomowe API cache
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# Zostawiam dekorator @cache_page tylko dla metody 'list' (na 10 minut)
@method_decorator(cache_page(600), name='list')
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        Nadpisuję metodę retrieve, aby użyć własnego klucza cache.
        Będzie cachowana na 1 minutę.
        """
        # Pobieram instancję obiektu, o który pyta użytkownik (np. produkt o id=1)
        instance = self.get_object()
        
        # Tworzę mój własny, unikalny klucz na podstawie klucza głównego (PK)
        cache_key = f'product_detail_{instance.pk}'
        
        # Próbuję pobrać dane z cache
        cached_data = cache.get(cache_key)
        
        if cached_data:
            # Jeśli są w cache, zwracam je od razu
            return Response(cached_data)

        # Jeśli nie ma w cache (cache miss), serializuję dane normalnie
        serializer = self.get_serializer(instance)
        data = serializer.data
        
        # Zapisuję wynik do cache na 60 sekund (1 minuta)
        cache.set(cache_key, data, timeout=60)
        
        return Response(data)

    def perform_update(self, serializer):
        """
        Nadpisuję operację zapisu przy aktualizacji (PUT/PATCH),
        aby unieważnić cache dla edytowanego obiektu.
        """
        # 1. Wykonuję standardowy zapis do bazy danych
        instance = serializer.save()
        
        # 2. Odtwarzam mój klucz dla tego konkretnego obiektu
        cache_key = f'product_detail_{instance.pk}'
        
        # 3. Usuwam klucz z cache, wymuszając pobranie świeżych danych przy kolejnym GET
        cache.delete(cache_key)
        
        
        
        # Testy:
        # 1. Wysyłam żądanie GET na [http://127.0.0.1:8000/api/products/1/]
        # Widok odpytuje bazę, pobiera dane i zapisuje je w naszym plikowym cache 
        # (FileBasedCache) pod spersonalizowanym kluczem product_detail_1 na 60 sekund.
        
        # 2. Wysyłam kolejne żądania GET pod ten sam adres.
        # Odpowiedź jest błyskawiczna – serwer zwraca zbuforowane dane.
        
        
        # 3. Wysyłam żądanie PATCH (lub robię to przez formularz przeglądarkowy DRF) 
        # na [http://127.0.0.1:8000/api/products/1/ 
        # zmieniając np. nazwę lub cenę produktu.
        
        # 4. Metoda perform_update zapisuje zmiany w bazie i 
        # natychmiast wywołuje cache.delete('product_detail_1').
        
        # 5. Wysyłam ponownie żądanie GET pod [http://127.0.0.1:8000/api/products/1/].
        # Pomimo faktu, że 60 sekund mogło jeszcze nie minąć, cache został unieważniony. 
        # Django notuje "cache miss", pobiera z bazy świeże, zaktualizowane przed chwilą 
        # dane, zwraca je i znów wrzuca do pamięci podręcznej z nową wartością.
        
            