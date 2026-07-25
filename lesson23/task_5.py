# Zadanie 5 – Domyślne sortowanie
# Ustaw domyślne sortowanie (ordering) listy samochodów od najnowszego rocznika do
# najstarszego.



# cars/admin.py
from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # Zadanie 2: Moje kolumny do wyświetlenia
    list_display = ('brand', 'model', 'year', 'is_available')

    # Zadanie 3: Dodaję pole wyszukiwania
    search_fields = ('brand', 'model')

    # Zadanie 4: Dodaję prawy panel z filtrami
    list_filter = ('is_available', 'year')

    # Zadanie 5: Ustawiam domyślne sortowanie od najnowszego rocznika do najstarszego (używam znaku minus)
    ordering = ('-year',)