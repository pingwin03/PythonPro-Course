# Zadanie 9 – Filtrowanie po kategorii
# Rozbuduj aplikację z produktami. Stwórz dynamiczną trasę /category/<int:category_id>/,
# która wyświetli tylko produkty należące do danej kategorii. W widoku musisz odfiltrować
# produkty na podstawie category_id przekazanego w URL


# do - myapp/views.py


from django.shortcuts import render, get_object_or_404
from .models import Product, Category 

# Nowy widok
def category_products_view(request, category_id):
    # Pobieramy konkretną kategorię po jej ID. Jeśli ktoś wpisze zły ID w URL, Django bezpiecznie zwróci błąd 404
    category = get_object_or_404(Category, id=category_id)
    
    # Filtrujemy produkty przypisane do tej właśnie kategorii
    products = Product.objects.filter(category=category)
    
    # Przekazujemy przefiltrowaną listę oraz sam obiekt kategorii do szablonu
    context = {
        'products': products,
        'category': category
    }
    return render(request, 'myapp/category_products.html', context)


# do - myproject/urls.py aktualizuje ścieżki

#  nowy widok do importów na górze pliku
from myapp.views import category_products_view 

urlpatterns = [
    
    # <int:category_id> to dynamiczny parametr. Django wyciągnie z URL-a liczbę (int) 
    # i przekaże ją do funkcji widoku jako argument "category_id"
    path('category/<int:category_id>/', category_products_view, name='category_products'),
]

# do - myapp/templates/myapp/ tworzę nowy plik o nazwie category_products.html i wpisuje:
    
    {% extends "myapp/base.html" %}

{% block title %}Produkty z kategorii: {{ category.name }}{% endblock %}

{% block content %}
    <h1>Kategoria: {{ category.name }}</h1>
    
    <!-- Sprawdzamy, czy kategoria ma w ogóle jakieś produkty -->
    {% if products %}
        <ul>
            {% for product in products %}
                <!-- Zakładam, że model Product ma pole price, jeśli nie, możesz usunąć ten fragment -->
                <li>{{ product.name }} - {{ product.price }} zł</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>Brak produktów w tej kategorii.</p>
    {% endif %}
    
    <br>
    <a href="/products/">Powrót do wszystkich produktów</a>
{% endblock %}



http://127.0.0.1:8000/category/1/