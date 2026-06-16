# Zadanie 7 – Wypełnij dane uczelni
# Napisz skrypt, który wypełni tabele studenci i audytoria przykładowymi danymi. Dodaj co
# najmniej 4 studentów i 3 audytoria.


import sqlite3

# Połączenie z bazą
conn = sqlite3.connect("uczelnia.db")
cursor = conn.cursor()

# Lista studentów (id_studenta, imie, nazwisko)
studenci = [
    (1, "Jan", "Kowalski"),
    (2, "Anna", "Nowak"),
    (3, "Piotr", "Wiśniewski"),
    (4, "Katarzyna", "Wójcik"),
    (5, "Marek", "Kamiński"),
    (6, "Agnieszka", "Lewandowski"),
]

# Lista audytoriów (id_audytorium, nazwa_budynku, numer_sali)
audytoria = [
    (1, "Budynek A", 101),
    (2, "Budynek A", 102),
    (3, "Budynek B", 201),
    (4, "Budynek B", 202),
    (5, "Budynek C", 301),
    (6, "Budynek C", 302),
]

# Dodanie studentów
cursor.executemany(
    """
    INSERT INTO studenci (id_studenta, imie, nazwisko)
    VALUES (?, ?, ?)
    """,
    studenci
)

# Dodanie audytoriów
cursor.executemany(
    """
    INSERT INTO audytoria (id_audytorium, nazwa_budynku, numer_sali)
    VALUES (?, ?, ?)
    """,
    audytoria
)

# Zapisanie zmian i zamknięcie połączenia
conn.commit()
conn.close()

print("Dodano 6 studentów i 6 audytoriów do bazy uczelnia.db")