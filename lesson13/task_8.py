# Zadanie 8 – Połącz tabele (Relacja)
# To zadanie wprowadza kluczowe pojęcie relacji. Chcemy przypisać studentów do
# audytoriów (np. na egzamin). Aby to zrobić, stwórz trzecią tabelę o nazwie przypisania w tej
# samej bazie uczelnia.db. Tabela powinna mieć strukturę:
# id_przypisania (INTEGER, klucz główny)
# id_studenta (INTEGER) – będzie to tzw. klucz obcy wskazujący na id_studenta w
# tabeli studenci .
# id_audytorium (INTEGER) – klucz obcy wskazujący na id_audytorium w tabeli
# audytoria 


import sqlite3

# Połączenie z bazą
conn = sqlite3.connect("uczelnia.db")
cursor = conn.cursor()

# Włączenie obsługi kluczy obcych w SQLite
conn.execute("PRAGMA foreign_keys = ON")

# Tworzenie tabeli przypisania
cursor.execute("""
CREATE TABLE IF NOT EXISTS przypisania (
    id_przypisania INTEGER PRIMARY KEY,
    id_studenta INTEGER NOT NULL,
    id_audytorium INTEGER NOT NULL,
    FOREIGN KEY (id_studenta) REFERENCES studenci(id_studenta),
    FOREIGN KEY (id_audytorium) REFERENCES audytoria(id_audytorium)
)
""")

# Zapisanie zmian i zamknięcie połączenia
conn.commit()
conn.close()

print("Utworzono tabelę przypisania z kluczami obcymi w bazie uczelnia.db")