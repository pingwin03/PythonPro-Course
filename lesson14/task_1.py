# Zadanie 1 – Liczba produktów
# Napisz skrypt, który połączy się z bazą sklep.db i policzy, ile jest wszystkich produktów w
# tabeli Produkty. Użyj funkcji COUNT().




import sqlite3
 
# Połączenie z bazą danych
conn = sqlite3.connect('sklep.db')
kursor = conn.cursor()
 
# Zapytanie SQL z funkcją COUNT()
kursor.execute("SELECT COUNT(*) FROM Produkty")
 
# Pobranie wyniku
liczba_produktow = kursor.fetchone()[0]
 
print(f"Liczba wszystkich produktów w tabeli Produkty: {liczba_produktow}")
 
# Zamknięcie połączenia
conn.close()
 