
# Zadanie 5 – Widok z ciasteczkiem
# Stwórz dwa widoki funkcyjne i podłącz je pod adresy /api/hello/ i /api/set-name/. Widok set-
# name powinien przyjmować parametr zapytania name (np. /api/set-name/?name=Anna) i
# ustawiać ciasteczko o nazwie user_name z podaną wartością. Widok hello powinien
# odczytywać to ciasteczko i zwracać komunikat "Witaj, [imię]!" lub "Witaj, Gość!", jeśli
# ciasteczko nie istnieje


# products_app/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def set_name_view(request):
    # Odczytuję parametr 'name' z mojego adresu URL (np. ?name=Anna)
    # Jeśli nikt nie poda parametru, domyślnie zapiszę wartość 'Gość'
    name = request.query_params.get('name', 'Gość')
    
    # Przygotowuję odpowiedź
    response = Response({"message": f"Ustawiono ciasteczko z imieniem: {name}"})
    
    # Ustawiam moje ciasteczko o nazwie 'user_name' z wartością pobraną z URL
    response.set_cookie('user_name', name)
    
    return response

@api_view(['GET'])
def hello_view(request):
    # Odczytuję wartość ciasteczka 'user_name' z mojego żądania
    # Jeśli ciasteczko nie istnieje, domyślnie zwrócę 'Gość'
    name = request.COOKIES.get('user_name', 'Gość')
    
    # Zwracam odpowiedź z odpowiednim powitaniem
    return Response({"message": f"Witaj, {name}!"})




# Podłączanie widoków do ścieżek URL

# my_api_project/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products_app import views 

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
    # Dodaję moje nowe ścieżki dla zadań z ciasteczkami
    path('api/set-name/', views.set_name_view),
    path('api/hello/', views.hello_view),
]

# Test:
http://127.0.0.1:8000/api/set-name/?name=Anna


http://127.0.0.1:8000/api/hello/