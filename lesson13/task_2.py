# Zadanie 2 – Dodaj książki
# Napisz skrypt, który doda do tabeli ksiazki (stworzonej w zadaniu 1) trzy dowolne książki.
# Użyj metody executemany do dodania wszystkich książek za jednym razem


import sqlite3

# Połączenie z bazą
conn = sqlite3.connect("biblioteka.db")
cursor = conn.cursor()

# Lista książek do dodania (krotki: tytul, autor, rok_wydania)
ksiazki = [
    ("Władca Pierścieni", "J.R.R. Tolkien", 1954),
    ("Duma i uprzedzenie", "Jane Austen", 1813),
    ("1984", "George Orwell", 1949),
]

# Dodanie wszystkich książek za pomocą executemany
cursor.executemany(
    """
    INSERT INTO ksiazki (tytul, autor, rok_wydania)
    VALUES (?, ?, ?)
    """,
    ksiazki
)

# Zapisanie zmian i zamknięcie połączenia
conn.commit()
conn.close()

print("Dodano 3 książki do tabeli ksiazki.")