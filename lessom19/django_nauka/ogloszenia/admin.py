# Zadanie 8

from django.contrib import admin
from .models import Ogloszenie  # Importujemy nasz nowo stworzony model



# Zadanie 10
# 1. Definiujemy klasę konfiguracyjną (ModelAdmin)
class OgloszenieAdmin(admin.ModelAdmin):
        list_display = ('tytul', 'cena', 'data_dodania')

# 2. Rejestrujemy model przekazując klasę konfiguracyjną jako drugi argument
admin.site.register(Ogloszenie, OgloszenieAdmin)