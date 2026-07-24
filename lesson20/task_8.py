# Zadanie 8 – Połącz modele relacją
# Stwórz nowy model Category z jednym polem name (CharField). Następnie zmodyfikuj
# model Product z zadania 3, dodając do niego pole category typu ForeignKey, które
# będzie wskazywało na model Category. Pamiętaj o migracjach



# do - myapp/models.py

from django.db import models

# 1. Tworzymy nowy model Category
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    # ... twoje dotychczasowe pola (np. name, price) ...
    
    # 2. Dodajemy relację do Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
    # przygotowanie do migracji.
    
    python manage.py makemigrations
    
    
    python manage.py migrate