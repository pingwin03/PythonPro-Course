# Zadanie 4 – Wyświetl dane w szablonie
# Stwórz widok, który pobierze kilka obiektów z bazy danych (możesz je dodać ręcznie przez
# python manage.py shell). Przekaż te obiekty do szablonu i wyświetl je w formie listy
# , używając pętli {% for %}.



# python manage.py shell


# tworzę szablon
<!DOCTYPE html>
<html>
<head>
    <title>Lista produktów</title>
</head>
<body>
    <h1>Nasze produkty</h1>
    <ul>
        {% for product in products %}
            <li>{{ product.name }} - {{ product.price }} zł</li>
        {% empty %}
            <li>Brak produktów w bazie.</li>
        {% endfor %}
    </ul>
</body>
</html>

# myapp/views.py łączenie widoku i bazy
from django.shortcuts import render
from .models import Product # Importujemy nasz model

def product_list_view(request):
    # Wyciągamy wszystkie produkty z bazy
    products = Product.objects.all()
    # Przekazujemy je do szablonu za pomocą słownika
    return render(request, 'myapp/product_list.html', {'products': products})
# nowa ścieżka do routingu
path('products/', views.product_list_view, name='product-list'),
]

http://127.0.0.1:8000/products/