# Zadanie 7 – Selektywne cachowanie w widoku
# Stwórz widok, który pobiera dane z dwóch źródeł: jedno zapytanie do bazy, które jest proste
# i szybkie, oraz drugie, które symuluje bardzo skomplikowane i długie obliczenia (użyj
# time.sleep(3)). Użyj niskopoziomowego API cache, aby zbuforować tylko wynik tych
# "skomplikowanych obliczeń", a nie całą odpowiedź widoku.




# store/views.py
import time
from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product

@api_view(['GET'])
def selective_cache_view(request):
    # 1. Proste i szybkie zapytanie do bazy danych (tego NIE cachuję)
    # Pobieram np. tylko 3 produkty
    fast_db_data = list(Product.objects.all()[:3].values())

    # 2. Skomplikowane i długie obliczenia (to CACHUJĘ)
    # Definiuję unikalny klucz dla mojego cache
    cache_key = 'my_heavy_computation'
    
    # Próbuję pobrać moje dane z cache
    complex_data = cache.get(cache_key)

    # Jeśli moich danych nie ma w cache (cache miss)
    if complex_data is None:
        # Wykonuję moją "drogą" operację i symuluję długie obliczenia używając sleep
        time.sleep(3)
        
        # Tworzę przykładowy wynik moich skomplikowanych obliczeń
        complex_data = {
            "value": 999,
            "description": "Wynik trudnego algorytmu"
        }
        
        # Zapisuję mój wynik do cache na 60 sekund
        cache.set(cache_key, complex_data, timeout=60)
        
        # Ustawiam flagę, żebym wiedział, skąd mam dane podczas testów
        data_source = "Wyliczono na żywo (trwało 3 sekundy)"
    else:
        # Zwracam wynik z cache!
        data_source = "Pobrano z cache (błyskawicznie!)"

    # 3. Łączę oba źródła w jedną odpowiedź
    response_data = {
        "db_data": fast_db_data,
        "complex_data": complex_data,
        "complex_data_source": data_source
    }

    return Response(response_data)




# cache_project/urls.py
from django.contrib import admin
from django.urls import path, include
from store.views import product_list, selective_cache_view # Importuję nowy widok

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('products/', product_list, name='product-list'),
    path('selective/', selective_cache_view, name='selective-cache'), # Dodaję nowy endpoint
]



# testy:
#     python manage.py runserver
    
#     http://127.0.0.1:8000/selective/
    
    
#     1 . Pierwsze żądanie: Strona "kręci się" i ładuje przez 3 sekundy. 
#     Odpowiedź pokazuje complex_data_source: "Wyliczono na żywo (trwało 3 sekundy)".
#     Pamięć podręczna zaliczyła "miss" i musiała wykonać przerwę wymuszoną przez time.sleep(3).
    
    
#     2. Drugie żądanie (odświeżenie): Strona ładuje się natychmiastowo! 
#     Zmienna źródłowa informuje: complex_data_source:
#         "Pobrano z cache (błyskawicznie!)"