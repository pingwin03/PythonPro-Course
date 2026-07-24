# Zadanie 3 – Podstawowy widok i szablon
# Zadania "Challenge"
# Napisz widok, który pobierze wszystkie obiekty Category z bazy. Stwórz prosty szablon
# HTML, który wyświetli nazwy wszystkich kategorii w formie listy nieuporządkowanej (
# ). Podłącz widok pod adres URL /categories/



# do - articles/views.py


from django.shortcuts import render
from .models import Category

def category_list_view(request):
    # Pobieramy wszystkie kategorie z bazy
    all_categories = Category.objects.all()
    
    # Przekazujemy dane do szablonu za pomocą słownika kontekstu
    context = {
        'categories': all_categories
    }
    return render(request, 'articles/category_list.html', context)


# W folderze aplikacji articles trzeba stworzyć strukturę katalogów templates/articles/, a w niej plik category_list.html


{% extends "base.html" %}

{% block content %}
    <h1>Lista Kategorii</h1>
    
    {% if categories %}
        <ul>
            {% for category in categories %}
                <li>{{ category.name }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>Brak kategorii w bazie.</p>
    {% endif %}
{% endblock %}

# do - le21/urls.py


from django.contrib import admin
from django.urls import path, include
from articles.views import category_list_view # Importujemy nasz nowy widok

urlpatterns = [
    path('admin/', admin.site.urls),
    # Podłączamy widok pod URL /categories/
    path('categories/', category_list_view, name='category-list'),
]