# Zadanie 2 – Najdroższy produkt
# Napisz skrypt, który znajdzie nazwę i cenę najdroższego produktu w sklepie. Użyj funkcji
# MAX()
import sqlite3
conn = sqlite3.connect('sklep.db')
cursor = conn.cursor()

# 1. Pobierz maksymalną cenę produktu z tabeli Produkty (użycie MAX())
cursor.execute("SELECT MAX(cena) FROM Produkty")
max_cena = cursor.fetchone()[0]

# 2. Pobierz nazwę produktu, który ma tę cenę
cursor.execute(
    "SELECT nazwa_produktu FROM Produkty WHERE cena = ?",
    (max_cena,)
)
nazwa_najdrozszy = cursor.fetchone()[0]

# 3. Wyświetl wynik
print(f"Najdroższy produkt: {nazwa_najdrozszy}, cena: {max_cena}")

conn.close()