# Zadanie 10 – Model powiązany i Inline
# Stwórz drugi model, Dealer, z polami name (CharField) i address (TextField). Połącz model
# Car z Dealer relacją ForeignKey. Następnie w panelu admina dla Dealera, wyświetl
# wszystkie przypisane do niego samochody w formie TabularInline.



## cars/models.py
from django.db import models

# Tworję nowy model Dealer, który posłuży nam do grupowania samochodów
class Dealer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa dealera")
    address = models.TextField(verbose_name="Adres")

    def __str__(self):
        return self.name

class Car(models.Model):
    # ... Twoje dotychczasowe pola (brand, model, year, photo, is_available itp.) ...
    
    # Dodaję powiązanie z Dealerem. 
    # Używam null=True i blank=True, żebym nie popsuł aut, które już mam w bazie.
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Dealer")
    
    
#   Migracja  
#     python manage.py makemigrations
# python manage.py migrate


# cars/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Car, Dealer  # Pamiętam, żeby zaimportować też model Dealer!

#


# --- Zadanie 10: Model powiązany i Inline ---

class CarInline(admin.TabularInline):
    model = Car
    extra = 1  # Określam, ile pustych wierszy ma pokazać Django do szybkiego dodawania aut


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    inlines = [CarInline]  # Tutaj spinam model Dealera z tabelką samochodów!



