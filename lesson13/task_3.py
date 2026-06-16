# Zadanie 3 – Wyświetl całą bibliotekę
# Napisz skrypt, który pobierze i wyświetli w konsoli wszystkie książki (wszystkie kolumny) z
# tabeli ksiazki.


import sqlite3

# Połączenie z bazą
conn = sqlite3.connect("biblioteka.db")
cursor = conn.cursor()

# Pobranie wszystkich książek
cursor.execute("SELECT * FROM ksiazki")
ksiazki = cursor.fetchall()

# Wyświetlenie nagłówka
print("ID | Tytuł | Autor | Rok wydania")
print("-" * 50)

# Wyświetlenie każdej książki
for ksiazka in ksiazki:
    id_, tytul, autor, rok = ksiazka
    print(f"{id_} | {tytul} | {autor} | {rok}")

# Zamknięcie połączenia
conn.close()