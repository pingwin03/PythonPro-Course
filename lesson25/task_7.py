# Zadanie 7 – API Kalkulatora
# (challenge)
# Stwórz widok funkcyjny (użyj dekoratora @api_view(['GET'])) pod adresem /api/calculate/.
# Widok powinien przyjmować trzy parametry zapytania: num1, num2 i operation (który może
# przyjąć wartości 'add', 'subtract', 'multiply', 'divide'). Widok powinien wykonać odpowiednią
# operację matematyczną i zwrócić wynik w formacie JSON, np. {"result": 15}. Zadbaj o
# obsługę błędów (np. dzielenie przez zero, niepoprawna operacja).




# products_app/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# ... (tutaj znajdują się wcześniejsze widoki i ViewSety)

@api_view(['GET'])
def calculate_view(request):
    # 1. Pobieram parametry z adresu URL (np. ?num1=10&num2=5&operation=add)
    num1 = request.query_params.get('num1')
    num2 = request.query_params.get('num2')
    operation = request.query_params.get('operation')

    # 2. Sprawdzam, czy użytkownik podał wszystkie wymagane parametry
    if num1 is None or num2 is None or operation is None:
        return Response(
            {"error": "Brakuje parametrów! Podaj num1, num2 oraz operation."}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    # 3. Próbuję przekonwertować parametry tekstowe na liczby zmiennoprzecinkowe (float)
    try:
        n1 = float(num1)
        n2 = float(num2)
    except ValueError:
        return Response(
            {"error": "Parametry num1 i num2 muszą być poprawnymi liczbami."}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    # 4. Wykonuję odpowiednią operację matematyczną
    if operation == 'add':
        result = n1 + n2
    elif operation == 'subtract':
        result = n1 - n2
    elif operation == 'multiply':
        result = n1 * n2
    elif operation == 'divide':
        # Obsługa błędu dzielenia przez zero
        if n2 == 0:
            return Response(
                {"error": "Błąd: Nie można dzielić przez zero!"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        result = n1 / n2
    else:
        # Obsługa niepoprawnej nazwy operacji
        return Response(
            {"error": "Nieznana operacja. Dozwolone to: add, subtract, multiply, divide."}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    # 5. Zwracam poprawny wynik w formacie JSON
    return Response({"result": result})

# REJESTRACJA ŚCIEŻKI:
# my_api_project/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products_app import views 

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'notes', views.NoteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
    # Dodaję ścieżkę do kalkulatora
    path('api/calculate/', views.calculate_view),
    
    # Moje ścieżki z poprzednich zadań
    path('api/set-name/', views.set_name_view),
    path('api/hello/', views.hello_view),
]

sORAWDZONE W PZREGLĄDARCE
Prawidłowe dodawanie: [http://127.0.0.1:8000/api/calculate/?num1=10&num2=5&operation=add]
Prawidłowe dzielenie: [http://127.0.0.1:8000/api/calculate/?num1=10&num2=2&operation=divide]
Test dzielenia przez zero: [http://127.0.0.1:8000/api/calculate/?num1=10&num2=0&operation=divide]
Test literówki w liczbie: [http://127.0.0.1:8000/api/calculate/?num1=10&num2=pięć&operation=add]
Test błędnej operacji: [http://127.0.0.1:8000/api/calculate/?num1=10&num2=5&operation=potegowanie]
