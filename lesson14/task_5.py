# Zadanie 5 – Lista klientów
# Napisz skrypt, który wyświetli imiona i adresy e-mail wszystkich klientów z tabeli Klienci.


import sqlite3
conn = sqlite3.connect('sklep.db')
cursor = conn.cursor()

# Pobierz i wyświetl imiona i adresy e-mail wszystkich klientów
cursor.execute("SELECT imie, email FROM Klienci")
klienci = cursor.fetchall()

print("Lista klientów:")
for imie, email in klienci:
    print(f"{imie} - {email}")

conn.close()