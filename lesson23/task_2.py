# Zadanie 2 – Konfiguracja kolumn
# Stwórz klasę CarAdmin i zarejestruj model Car z jej pomocą (używając dekoratora). W
# list_display wyświetl tylko markę, model, rok produkcji oraz status dostępności
# (is_available)



# cars/admin.py
from django.contrib import admin
from .models import Car

# Używam dekoratora do rejestracji modelu, tak jak prosi Zadanie 2
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # Określam kolumny do wyświetlenia: markę, model, rok produkcji oraz status dostępności
    list_display = ('brand', 'model', 'year', 'is_available')