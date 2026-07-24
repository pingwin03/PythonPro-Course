# Zadanie 2 – Dodawanie danych
# Używając konsoli Django (python manage.py shell), stwórz 3 różne obiekty modelu
# Category (np. "Sport", "Technologia", "Kultura") i zapisz je w bazie danych.


# w terminali:
    
    python manage.py shell
    
    
    
    
from articles.models import Category

# Metoda create() od razu tworzy obiekt i zapisuje go w bazie (odpowiednik SQL INSERT INTO)
Category.objects.create(name="Sport")
Category.objects.create(name="Technologia")
Category.objects.create(name="Kultura")

# weryfikacja czy poprawnie dodały się do bazy:
print(Category.objects.all())

# Aby wyjść z interaktywnej konsoli:
exit()