# Zadanie 3 – Pierwszy ViewSet i Router
# (proste)
# Stwórz ModelViewSet dla modelu Product. Podłącz go do głównego pliku urls.py za
# pomocą DefaultRouter pod adresem /api/products/. Uruchom serwer i wejdź na adres
# http://127.0.0.1:8000/api/products/ w przeglądarce. Co widzisz?



# products_app/views.py
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

# Tworzę mój widok dziedziczący po ModelViewSet, aby obsłużyć żądania HTTP
class ProductViewSet(viewsets.ModelViewSet):
    # Określam, jakie dane z bazy mają być dostępne dla tego widoku
    queryset = Product.objects.all()
    
    # Wskazuję, jakiego serializatora użyć do "tłumaczenia" tych danych na JSON
    serializer_class = ProductSerializer
    
    
    
    # Podłączanie routera w głównym urls.py
    
    # my_api_project/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Importuję widoki z mojej aplikacji, aby móc je zarejestrować
from products_app import views 

# Tworzę instancję routera, który zajmie się adresami
router = DefaultRouter()

# Rejestruję mój ViewSet pod ścieżką 'products'
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Podłączam wszystkie wygenerowane adresy z routera pod prefiks 'api/'
    path('api/', include(router.urls)),
]


# http://127.0.0.1:8000/api/products/


# Widzę tzw. Browsable API (Przeglądarkowe API), czyli bardzo przyjazny dla programisty interfejs graficzny wygenerowany automatycznie 
# przez Django REST Framework. Na tej stronie widzę:

# Nagłówek HTTP wskazujący na pomyślne żądanie GET (status 200 OK).

# Główne okno odpowiedzi zwracające pustą listę [] w formacie JSON (ponieważ moja baza danych nie ma jeszcze żadnych zapisanych produktów).

# Na samym dole ekranu widzę wygenerowany, interaktywny formularz HTML z polami "Name" i "Price". 
# Pozwala on na łatwe stworzenie nowego produktu i wysłanie zapytania POST bezpośrednio z okna przeglądarki,
# bez potrzeby używania dodatkowych narzędzi.