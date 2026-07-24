# Zadanie 6 – Widok szczegółów
# Stwórz nowy widok category_detail_view, który będzie przyjmował w URL-u ID kategorii
# (np. /categories/1/). Widok powinien pobrać z bazy danych tylko ten jeden, konkretny obiekt
# Category i przekazać go do nowego szablonu category_detail.html, który wyświetli jego
# nazwę w nagłówku
# .
# Wskazówka: path('categories/<int:pk>/', ...) w urls.py i
# def my_view(request, pk): ... w views.py.


# do - articles/views.py


from django.shortcuts import render
from .models import Category


def category_detail_view(request, pk):
    # Pobieramy z bazy konkretną kategorię na podstawie ID (pk)
    category = Category.objects.get(id=pk)
    
    # Przekazujemy pobraną kategorię do szablonu
    context = {
        'category': category
    }
    
    return render(request, 'articles/category_detail.html', context)


# do - le21/urls.py



from django.contrib import admin
from django.urls import path
#  nowy widok!
from articles.views import category_list_view, category_detail_view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', category_list_view, name='category-list'),
    
    # Nowa ścieżka dla szczegółów kategorii (oczekuje liczby całkowitej <int:pk>)
    path('categories/<int:pk>/', category_detail_view, name='category-detail'),
]


# do - articles/templates/articles/ tworzę nowy plik o nazwie category_detail.html

{% extends "base.html" %}

{% block content %}
    <!-- Wyświetlanie nazwy kategorii w nagłówku H1 -->
    <h1>{{ category.name }}</h1>
    
    <!-- Opcjonalny przycisk powrotu do listy, żeby łatwiej się nawigowało -->
    <a href="/categories/" class="btn btn-secondary mt-3">Powrót do listy</a>
{% endblock %}



http://127.0.0.1:8000/categories/1/