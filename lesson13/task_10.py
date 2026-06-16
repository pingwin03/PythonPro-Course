# Zadanie 10 – Funkcja wyszukująca z JOIN
# Napisz funkcję w Pythonie znajdz_sale_studenta(nazwisko), która przyjmuje nazwisko
# studenta jako argument. Funkcja powinna połączyć się z bazą, a następnie znaleźć i
# wyświetlić informację, w którym budynku i w jakiej sali znajduje się dany student.

# Tip
# Aby rozwiązać to zadanie, będziesz potrzebować klauzuli JOIN w zapytaniu SELECT.
# Pozwala ona łączyć wiersze z dwóch lub więcej tabel na podstawie powiązanych
# kolumn


import sqlite3

def znajdz_sale_studenta(nazwisko):
    """
    Szuka studenta po nazwisku i wyświetla jego salę oraz budynek.
    """
    conn = sqlite3.connect("uczelnia.db")
    cursor = conn.cursor()

    # Zapytanie z JOIN łączące trzy tabele
    cursor.execute("""
        SELECT 
            s.imie,
            s.nazwisko,
            a.nazwa_budynku,
            a.numer_sali
        FROM studenci s
        JOIN przypisania p ON s.id_studenta = p.id_studenta
        JOIN audytoria a ON p.id_audytorium = a.id_audytorium
        WHERE s.nazwisko = ?
    """, (nazwisko,))

    wynik = cursor.fetchone()
    conn.close()

    if wynik:
        imie, nazwisko, budynek, sala = wynik
        print(f"Student: {imie} {nazwisko}")
        print(f"Budynek: {budynek}")
        print(f"Sala: {sala}")
    else:
        print(f"Nie znaleziono studenta o nazwisku: {nazwisko}")


# Przykładowe wywołanie
znajdz_sale_studenta("Kowalski")