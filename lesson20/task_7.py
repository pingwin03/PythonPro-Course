# Zadanie 7 – Formularz dodawania produktu
# Bazując na modelu Product z zadania 3, stwórz formularz Django (ProductForm), który
# pozwoli na dodawanie nowych produktów. Stwórz widok, który będzie obsługiwał ten
# formularz (wyświetlanie pustego formularza metodą GET i przetwarzanie danych
# metodą POST). Po poprawnym zapisaniu produktu, przekieruj użytkownika na stronę z
# listą produktów



# do - myapp tworzę nowy plik o nazwie forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # Zakładam, że model Product ma pola 'name' i 'price' na podstawie wcześniejszych zadań
        fields = ['name', 'price']
        
        
# do - myapp/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm

def add_product_view(request):
    if request.method == 'POST':
        # Jeśli użytkownik wysłał dane, wypełniamy formularz tymi danymi
        form = ProductForm(request.POST)
        if form.is_valid():
            # Jeśli dane są poprawne, zapisujemy nowy produkt w bazie
            form.save()
            # Przekierowujemy na stronę z listą produktów 
            return redirect('/products/') 
    else:
        # Jeśli użytkownik dopiero wszedł na stronę (GET), pokazujemy pusty formularz
        form = ProductForm()
    
    return render(request, 'myapp/add_product.html', {'form': form})

# do - myproject/urls.py

from myapp.views import info_view, product_list_view, note_list_view, note_detail_view, add_product_view

urlpatterns = [
    path('add-product/', add_product_view, name='add_product'),
]

# do - myapp/templates/myapp/  add_product.html
{% extends "myapp/base.html" %}

{% block title %}Dodaj produkt{% endblock %}

{% block content %}
    <h1>Dodaj nowy produkt</h1>
    
    <!-- method="POST" oznacza, że dane z formularza będą wysłane bezpiecznie do serwera -->
    <form method="POST">
        {% csrf_token %}
        
        <!-- {{ form.as_p }} wygeneruje cały formularz i owinie każde pole w tagi paragrafu <p> -->
        {{ form.as_p }}
        
        <button type="submit">Zapisz produkt</button>
    </form>
    <br>
    <a href="/products/">Powrót do listy produktów</a>
{% endblock %}

http://127.0.0.1:8000/add-product/