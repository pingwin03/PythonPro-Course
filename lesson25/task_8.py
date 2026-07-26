# Zadanie 8 – Filtrowanie i wyszukiwanie
# (challenge)
# W ViewSet dla produktów (z zadania 2) zaimplementuj filtrowanie po cenie. Chcemy móc
# wysyłać zapytania takie jak /api/products/?min_price=100&max_price=200, które zwrócą
# produkty w danym przedziale cenowym. Wskazówka: nadpisz metodę get_queryset w
# swoim ViewSet


# products_app/views.py   zmieniam ProductViewSet z zadania 3

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    # Usuwam linijkę: queryset = Product.objects.all()
    # Zostawiam tylko powiązanie z serializatorem
    serializer_class = ProductSerializer

    # Nadpisuję metodę get_queryset, która decyduje, jakie dane zwrócić
    def get_queryset(self):
        # 1. Zaczynam od pobrania wszystkich produktów z bazy
        queryset = Product.objects.all()
        
        # 2. Próbuję odczytać parametry 'min_price' i 'max_price' z adresu URL
        # self.request to odpowiednik 'request' z widoków funkcyjnych
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        
        # 3. Jeśli użytkownik podał cenę minimalną, filtruję wyniki
        if min_price is not None:
            # W Django ORM 'price__gte' oznacza "price Greater Than or Equal" (większe lub równe)
            queryset = queryset.filter(price__gte=min_price)
            
        # 4. Jeśli użytkownik podał cenę maksymalną, nakładam kolejny filtr
        if max_price is not None:
            # 'price__lte' oznacza "price Less Than or Equal" (mniejsze lub równe)
            queryset = queryset.filter(price__lte=max_price)
            
        # 5. Na koniec zwracam gotową (przefiltrowaną) listę produktów
        return queryset
    
    
    testowaneie w POSTMAN: dział
    http://127.0.0.1:8000/api/products/
    http://127.0.0.1:8000/api/products/?min_price=100
    http://127.0.0.1:8000/api/products/?max_price=200
    http://127.0.0.1:8000/api/products/?min_price=100&max_price=200