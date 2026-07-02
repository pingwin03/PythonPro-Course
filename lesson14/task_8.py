# Zadanie 8 – Kategorie z liczbą produktów
# Napisz zapytanie, które wyświetli nazwę każdej kategorii oraz liczbę produktów należących
# do tej kategorii. Użyj JOIN, COUNT() oraz GROUP BY.


import sqlite3

conn = sqlite3.connect('sklep.db')
cursor = conn.cursor()

# Wyświetl nazwę każdej kategorii oraz liczbę produktów należących do tej kategorii
# Użycie JOIN + COUNT() + GROUP BY
cursor.execute("""
    SELECT k.nazwa_kategorii, COUNT(p.id_produktu)
    FROM Kategorie k
    JOIN Produkty p ON k.id_kategorii = p.id_kategorii
    GROUP BY k.id_kategorii, k.nazwa_kategorii
""")
kategorie_z_liczba = cursor.fetchall()

print("Kategorie z liczbą produktów:")
for nazwa, liczba in kategorie_z_liczba:
    print(f"{nazwa} - {liczba} produktów")

conn.close()