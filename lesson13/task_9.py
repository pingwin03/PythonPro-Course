# Zadanie 9 – Dokonaj przypisań
# Napisz skrypt, który dokona przypisań. Dla każdego studenta z tabeli studenci dodaj wpis
# do tabeli przypisania, łącząc go z jednym z audytoriów


import sqlite3

# Połączenie z bazą
conn = sqlite3.connect("uczelnia.db")
cursor = conn.cursor()

# Włączenie obsługi kluczy obcych
conn.execute("PRAGMA foreign_keys = ON")

# Pobranie wszystkich studentów
cursor.execute("SELECT id_studenta FROM studenci")
studenci = cursor.fetchall()

# Pobranie wszystkich audytoriów
cursor.execute("SELECT id_audytorium FROM audytoria")
audytoria = cursor.fetchall()

# Jeśli nie ma danych, informujemy
if not studenci:
    print("Brak studentów w bazie.")
    conn.close()
    exit()

if not audytoria:
    print("Brak audytoriów w bazie.")
    conn.close()
    exit()

# Tworzenie przypisań: każdy student do jednego audytorium
przypisania = []
for i, (id_studenta,) in enumerate(studenci):
    # Wybór audytorium w cyklu (modulo liczba audytoriów)
    id_audytorium = audytoria[i % len(audytoria)][0]
    przypisania.append((id_studenta, id_audytorium))

# Dodanie wszystkich przypisań za pomocą executemany
cursor.executemany(
    """
    INSERT INTO przypisania (id_studenta, id_audytorium)
    VALUES (?, ?)
    """,
    przypisania
)

# Zapisanie zmian i zamknięcie połączenia
conn.commit()
conn.close()

print(f"Dokonano {len(przypisania)} przypisań studentów do audytoriów.")