# Zadanie 1 – Stwórz tabelę książek
# Napisz skrypt, który połączy się z bazą biblioteka.db i stworzy w niej tabelę ksiazki. Tabela
# powinna mieć następujące kolumny:
# id (INTEGER, klucz główny)
# tytul (TEXT, nie może być pusty)
# autor (TEXT, nie może być pusty)
# rok_wydania (INTEGER)


import sqlite3

# Połączenie z bazą (lub utworzenie, jeśli nie istnieje)
conn = sqlite3.connect("biblioteka.db")
cursor = conn.cursor()

# Tworzenie tabeli ksiazki
cursor.execute("""
CREATE TABLE IF NOT EXISTS ksiazki (
    id INTEGER PRIMARY KEY,
    tytul TEXT NOT NULL,
    autor TEXT NOT NULL,
    rok_wydania INTEGER
)
""")

# Zapisanie zmian i zamknięcie połączenia
conn.commit()
conn.close()

print("Tabela ksiazki została utworzona w bazie biblioteka.db.")