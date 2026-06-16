# Zadanie 4 – Wyszukaj książki autora
# Napisz skrypt, który pobierze i wyświetli tylko te książki z tabeli ksiazki, które zostały
# napisane przez Twojego ulubionego autora.







import sqlite3

# Połączenie z bazą
conn = sqlite3.connect("biblioteka.db")
cursor = conn.cursor()

# Ustaw autora, którego książki chcesz wyszukać
ulubiony_autor = "J.R.R. Tolkien"

# Pobranie książek danego autora
cursor.execute(
    "SELECT * FROM ksiazki WHERE autor = ?",
    (ulubiony_autor,)
)
ksiazki = cursor.fetchall()

# Wyświetlenie nagłówka
print(f"Książki autorstwa: {ulubiony_autor}")
print("ID | Tytuł | Autor | Rok wydania")
print("-" * 50)

# Wyświetlenie każdej książki
if ksiazki:
    for ksiazka in ksiazki:
        id_, tytul, autor, rok = ksiazka
        print(f"{id_} | {tytul} | {autor} | {rok}")
else:
    print("Nie znaleziono książek tego autora.")

# Zamknięcie połączenia
conn.close()