# Zadanie 6 – Produkty droższe od średniej
# Napisz skrypt, który wyświetli nazwy i ceny wszystkich produktów, których cena jest wyższa
# niż średnia cena wszystkich produktów w sklepie. Wykorzystaj podzapytanie

import sqlite3
conn = sqlite3.connect('sklep.db')
cursor = conn.cursor()

# Wyświetl nazwy i ceny produktów, których cena jest wyższa niż średnia cena wszystkich produktów
# Użycie podzapytania w klauzuli WHERE
cursor.execute("""
    SELECT nazwa_produktu, cena
    FROM Produkty
    WHERE cena > (SELECT AVG(cena) FROM Produkty)
""")
produkty_drozsze = cursor.fetchall()

print("Produkty droższe od średniej ceny:")
for nazwa, cena in produkty_drozsze:
    print(f"{nazwa} - {cena}")

conn.close()