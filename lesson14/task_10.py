# Zadanie 10 – Prosta symulacja ORM
# Stwórz klasę Produkt w Pythonie z atrybutami id_produktu, nazwa_produktu i cena.
# Następnie napisz funkcję pobierz_wszystkie_produkty(), która połączy się z bazą danych,
# pobierze wszystkie produkty i zwróci listę obiektów klasy Produkt. To ćwiczenie pokaże Ci,
# jak ORM automatyzuje mapowanie wierszy na obiekty.

import sqlite3

class Produkt:
    def __init__(self, id_produktu, nazwa_produktu, cena):
        self.id_produktu = id_produktu
        self.nazwa_produktu = nazwa_produktu
        self.cena = cena

    def __repr__(self):
        return f"Produkt(id_produktu={self.id_produktu}, nazwa_produktu='{self.nazwa_produktu}', cena={self.cena})"


def pobierz_wszystkie_produkty():
    conn = sqlite3.connect("sklep.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id_produktu, nazwa_produktu, cena
        FROM Produkty
    """)
    wiersze = cursor.fetchall()

    produkty = []
    for wiersz in wiersze:
        produkt = Produkt(wiersz[0], wiersz[1], wiersz[2])
        produkty.append(produkt)

    conn.close()
    return produkty


# Przykład użycia:
wszystkie_produkty = pobierz_wszystkie_produkty()
for produkt in wszystkie_produkty:
    print(produkt)