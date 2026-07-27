# Zadanie 3 – Cachowanie widoku API
# Wybierz jeden z istniejących, prostych widoków GET w Twoim API (np. lista obiektów). Za
# pomocą dekoratora @cache_page ustaw cache na 60 sekund. Użyj Django Debug Toolbar,
# aby zweryfikować, że przy pierwszym żądaniu jest "cache miss", a przy kolejnych (w ciągu
# 60 sekund) jest "cache hit"


# store/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
    
python manage.py makemigrations
oraz
python manage.py migrate



# store/views.py
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product

# Zgodnie z poleceniem dodaję dekorator ustawiający czas trwania cache na 60 sekund.
@cache_page(60) 
@api_view(['GET'])
def product_list(request):
    # Ta część kodu wykona się tylko wtedy, gdy odpowiedzi nie ma w cache (cache miss).
    products = Product.objects.all()
    
    # Ręcznie serializuję dane na potrzeby tego prostego zadania, tak jak w lekcji.
    data = {"products": list(products.values())}
    
    # Zwracam odpowiedź[cite: 1].
    return Response(data)


# cache_project/urls.py
from django.contrib import admin
from django.urls import path, include
from store.views import product_list # Importuję mój nowy widok

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('products/', product_list, name='product-list'), # Dodaję endpoint
]


python manage.py runserver


http://127.0.0.1:8000/products/ 