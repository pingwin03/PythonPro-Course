# Zadanie 7 – Pole tylko do odczytu
# W panelu admina, w widoku edycji pojedynczego samochodu, spraw, aby pole year było
# polem tylko do odczytu (readonly_fields).
# (challenge)


# cars/admin.py
from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # Zadanie 2 i 6: Dodaję moją nową metodę 'full_name' do kolumn
    list_display = ('brand', 'model', 'full_name', 'year', 'is_available')

    # Zadanie 3: Dodaję pole wyszukiwania
    search_fields = ('brand', 'model')

    # Zadanie 4: Dodaję panel z filtrami
    list_filter = ('is_available', 'year')

    # Zadanie 5: Ustawiam domyślne sortowanie
    ordering = ('-year',)

    # --- Zadanie 7: Pole tylko do odczytu ---
    # Blokuję możliwość edycji roku produkcji w widoku szczegółów samochodu
    readonly_fields = ('year',)

    # --- Zadanie 6: Pole generowane dynamicznie ---
    def full_name(self, obj):
        # Łączę wartości z pól brand i model
        return f"{obj.brand} {obj.model}"
    
    # Ustawiam nagłówek kolumny dla mojej nowej metody
    full_name.short_description = 'Pełna nazwa'