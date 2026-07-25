# Zadanie 1 – Podstawowa rejestracja
# Zadania "Challenge"
# Zarejestruj model Car w panelu administracyjnym, tak aby był w nim widoczny. Użyj
# najprostszej metody admin.site.register().




# cars/admin.py
from django.contrib import admin
from .models import Car

# Rejestruję mój model Car przy użyciu najprostszej metody, aby pojawił się w głównym widoku panelu admina
admin.site.register(Car)



http://127.0.0.1:8000/admin/