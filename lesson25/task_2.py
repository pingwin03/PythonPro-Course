# Zadanie 2 – Prosty model i serializator
# (proste)
# W nowej aplikacji Django stwórz model Product z polami name (CharField) i price
# (DecimalField). Następnie stwórz dla niego ModelSerializer, który będzie uwzględniał oba te
# pola oraz id.


    
    # Dodaję moją nowo utworzoną aplikację
    'products_app',


# products_app/models.py
from django.db import models

class Product(models.Model):
    # Tworzę pole na nazwę produktu (wymaga określenia max_length)
    name = models.CharField(max_length=255)
    
    # Tworzę pole na cenę produktu (wymaga określenia max_digits i decimal_places)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Dodaję metodę __str__, aby mój obiekt ładnie wyświetlał się w panelu admina
    def __str__(self):
        return self.name



# Migracja
# W terminalu przygotowuję i wykonuję migracje
python manage.py makemigrations
python manage.py migrate



# products_app/serializers.py
from rest_framework import serializers
from .models import Product

# Tworzę mój serializator, który dziedziczy po ModelSerializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        # Wskazuję, który z moich modeli ma być serializowany
        model = Product
        
        # Wymieniam w liście pola, które chcę uwzględnić, wliczając w to automatyczne 'id'
        fields = ['id', 'name', 'price']