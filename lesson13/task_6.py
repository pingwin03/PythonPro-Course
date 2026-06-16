# Zadanie 6 – Dwie tabele: Studenci i Audytoria
# Napisz skrypt, który w nowej bazie uczelnia.db stworzy dwie tabele:
# studenci z kolumnami: id_studenta (klucz główny), imie (TEXT), nazwisko
# (TEXT).
# audytoria z kolumnami: id_audytorium (klucz główny), nazwa_budynku (TEXT),
# numer_sali (INTEGER).



import sqlite3

# Połączenie z bazą (utworzy ją, jeśli nie istnieje)
conn = sqlite3.connect("uczelnia.db")
cursor = conn.cursor()

# Tworzenie tabeli studenci
cursor.execute("""
CREATE TABLE IF NOT EXISTS studenci (
    id_studenta INTEGER PRIMARY KEY,
    imie TEXT NOT NULL,
    nazwisko TEXT NOT NULL
)
""")

# Tworzenie tabeli audytoria
cursor.execute("""
CREATE TABLE IF NOT EXISTS audytoria (
    id_audytorium INTEGER PRIMARY KEY,
    nazwa_budynku TEXT NOT NULL,
    numer_sali INTEGER NOT NULL
)
""")

# Zapisanie zmian i zamknięcie połączenia
conn.commit()
conn.close()

print("Utworzono tabele: studenci i audytoria w bazie uczelnia.db")