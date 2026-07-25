# Zadanie 3 – Dodanie wyszukiwania
# Do klasy CarAdmin dodaj search_fields, aby umożliwić wyszukiwanie samochodów po
# marce i modelu.


# cars/admin.py
from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # Zadanie 2: Moje kolumny do wyświetlenia
    list_display = ('brand', 'model', 'year', 'is_available')

    # Zadanie 3: Dodaję pole wyszukiwania, które przeszukuje markę i model
    search_fields = ('brand', 'model')