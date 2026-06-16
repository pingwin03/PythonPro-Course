# Zadanie 5 – Zaktualizuj rok wydania
# Wybierz jedną z dodanych książek i napisz skrypt, który zaktualizuje jej rok_wydania na
# inną wartość. Po aktualizacji wyświetl dane tej książki, aby potwierdzić, że zmiana się
# powiodła.




import sqlite3

# Połączenie z bazą
conn = sqlite3.connect("biblioteka.db")
cursor = conn.cursor()

# Wybierz książkę do aktualizacji (np. id = 1)
ksiazka_id = 1
nowy_rok = 2024

# Wyświetl dane książki przed aktualizacją
cursor.execute("SELECT * FROM ksiazki WHERE id = ?", (ksiazka_id,))
ksiazka_przed = cursor.fetchone()

if ksiazka_przed is None:
    print(f"Nie znaleziono książki o id = {ksiazka_id}.")
    conn.close()
else:
    id_, tytul, autor, rok = ksiazka_przed
    print("Przed aktualizacją:")
    print(f"ID: {id_}, Tytuł: {tytul}, Autor: {autor}, Rok: {rok}")

    # Aktualizacja roku wydania
    cursor.execute(
        "UPDATE ksiazki SET rok_wydania = ? WHERE id = ?",
        (nowy_rok, ksiazka_id)
    )
    conn.commit()

    # Wyświetl dane książki po aktualizacji
    cursor.execute("SELECT * FROM ksiazki WHERE id = ?", (ksiazka_id,))
    ksiazka_po = cursor.fetchone()

    id_, tytul, autor, rok = ksiazka_po
    print("\nPo aktualizacji:")
    print(f"ID: {id_}, Tytuł: {tytul}, Autor: {autor}, Rok: {rok}")

# Zamknięcie połączenia
conn.close()