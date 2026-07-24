# Zadanie 5 – Filtrowanie w shellu
# W konsoli Django (shell) napisz zapytanie ORM, które pobierze tylko kategorię o nazwie
# "Sport". Użyj metody get().

# w terminalu
python manage.py shell



from articles.models import Category

# Pobieramy dokładnie jedną kategorię o nazwie "Sport"
sport_category = Category.objects.get(name="Sport")

# Aby sprawdzić wynik i upewnić się, że pobrano właściwy obiekt:
print(sport_category)