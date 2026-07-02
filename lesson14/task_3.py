# Zadanie 3 – Suma wartości
# Oblicz i wyświetl łączną wartość wszystkich produktów z kategorii "Elektronika". Użyj funkcji
# SUM() oraz klauzuli WHERE z JOIN

import sqlite3
conn = sqlite3.connect('sklep.db')
cursor = conn.cursor()

# Oblicz łączną wartość produktów z kategorii "Elektronika"
# Użycie SUM() + JOIN + WHERE
cursor.execute("""
    SELECT SUM(p.cena)
    FROM Produkty p
    JOIN Kategorie k ON p.id_kategorii = k.id_kategorii
    WHERE k.nazwa_kategorii = 'Elektronika'
""")
suma_wartosci = cursor.fetchone()[0]

print(f"Lączna wartość produktów z kategorii \"Elektronika\": {suma_wartosci}")

conn.close()