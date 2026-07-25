# Zadanie 6 – Pole generowane dynamicznie
# Stwórz w CarAdmin niestandardową metodę full_name, która zwróci połączony string z
# marki i modelu (np. "Ford Mustang"). Dodaj tę metodę do list_display i ustaw jej nagłówek
# (short_description) na "Pełna nazwa".


# cars/admin.py
from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # Zadanie 2 i 6: Dodaję moją nową metodę 'full_name' do kolumn wyświetlanych na liście
    list_display = ('brand', 'model', 'full_name', 'year', 'is_available')

    # Zadanie 3: Dodaję pole wyszukiwania
    search_fields = ('brand', 'model')

    # Zadanie 4: Dodaję prawy panel z filtrami
    list_filter = ('is_available', 'year')

    # Zadanie 5: Ustawiam domyślne sortowanie
    ordering = ('-year',)

    # --- Zadanie 6: Pole generowane dynamicznie ---
    def full_name(self, obj):
        # Łączę wartości z pól brand i model w jeden ciąg znaków, używając f-stringa
        return f"{obj.brand} {obj.model}"
    
    # Ustawiam przyjazny nagłówek kolumny dla mojej nowej metody
    full_name.short_description = 'Pełna nazwa'