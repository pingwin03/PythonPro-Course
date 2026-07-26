
from rest_framework import viewsets
from .models import Product, Note, Author, Book
from .serializers import ProductSerializer, NoteSerializer, AuthorSerializer, BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Tworzę mój widok dziedziczący po ModelViewSet, aby obsłużyć żądania HTTP
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
    
class NoteViewSet(viewsets.ModelViewSet):
    # Pobieram wszystkie notatki z bazy i sortuję je od najnowszej
    queryset = Note.objects.all().order_by('-created_at')
    
    # Podpinam odpowiedni serializator do "tłumaczenia"
    serializer_class = NoteSerializer
    
    
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



class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer