# Zadanie 9 – Funkcja do wyszukiwania produktów
# Napisz w Pythonie funkcję znajdz_produkty_w_kategorii(nazwa_kategorii), która przyjmuje
# jako argument nazwę kategorii i zwraca listę krotek (nazwa_produktu, cena) dla wszystkich
# produktów w tej kategorii




import sqlite3

def znajdz_produkty_w_kategorii(nazwa_kategorii):
    conn = sqlite3.connect("sklep.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.nazwa_produktu, p.cena
        FROM Produkty p
        JOIN Kategorie k ON p.id_kategorii = k.id_kategorii
        WHERE k.nazwa_kategorii = ?
    """, (nazwa_kategorii,))

    wyniki = cursor.fetchall()
    conn.close()
    return wyniki


# Przykład użycia:
produkty = znajdz_produkty_w_kategorii("Elektronika")
print(produkty)