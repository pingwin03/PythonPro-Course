# Zadanie 4 – Średnia cena książki
# Napisz zapytanie, które obliczy średnią cenę produktów w kategorii "Książki". Użyj AVG().


import sqlite3
conn = sqlite3.connect('sklep.db')
cursor = conn.cursor()

# Oblicz średnią cenę produktów w kategorii "Książki"
# Użycie AVG() + JOIN + WHERE
cursor.execute("""
    SELECT AVG(p.cena)
    FROM Produkty p
    JOIN Kategorie k ON p.id_kategorii = k.id_kategorii
    WHERE k.nazwa_kategorii = 'Książki'
""")
srednia_cena = cursor.fetchone()[0]

print(f"Średnia cena książki: {srednia_cena}")

conn.close()