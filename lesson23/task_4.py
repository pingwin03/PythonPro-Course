# Zadanie 4 – Dodanie filtrów
# Dodaj list_filter, aby można było filtrować samochody po polu is_available oraz year.


# cars/admin.py
from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # Zadanie 2: Moje kolumny do wyświetlenia
    list_display = ('brand', 'model', 'year', 'is_available')

    # Zadanie 3: Dodaję pole wyszukiwania
    search_fields = ('brand', 'model')

    # Zadanie 4: Dodaję prawy panel z filtrami po statusie dostępności i roku produkcji
    list_filter = ('is_available', 'year')