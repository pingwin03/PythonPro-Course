# Zadanie 3 – Stwórz prosty model
# W pliku models.py stwórz model o nazwie Product. Model powinien mieć trzy pola: name
# (CharField, max 100 znaków), description (TextField) oraz price (DecimalField, z
# max_digits=6, decimal_places=2). Nie zapomnij o stworzeniu i zaaplikowaniu migracji


# do myapp/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    
    
    
    
    
    #  w terminalu migracja:
        python manage.py makemigrations
        
        
        python manage.py migrate