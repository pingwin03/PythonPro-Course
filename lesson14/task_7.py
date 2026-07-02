# Zadanie 7 – Zamówienia Anny Nowak
# Napisz skrypt, który wyświetli nazwy wszystkich produktów zamówionych przez klienta o
# imieniu 'Anna Nowak'. Będziesz potrzebować połączyć dane z czterech tabel: Klienci,
# Zamowienia, Zamowienia_Produkty i Produkty

import sqlite3
conn = sqlite3.connect('sklep.db')
cursor = conn.cursor()

# Wyświetl nazwy wszystkich produktów zamówionych przez klienta o imieniu 'Anna Nowak'
# Połączenie czterech tabel: Klienci, Zamowienia, Zamowienia_Produkty, Produkty
cursor.execute("""
    SELECT p.nazwa_produktu
    FROM Klienci k
    JOIN Zamowienia z ON k.id_klienta = z.id_klienta
    JOIN Zamowienia_Produkty zp ON z.id_zamowienia = zp.id_zamowienia
    JOIN Produkty p ON zp.id_produktu = p.id_produktu
    WHERE k.imie = 'Anna Nowak'
""")
produkty_anna = cursor.fetchall()

print("Produkty zamówione przez Annę Nowak:")
for nazwa in produkty_anna:
    print(nazwa[0])

conn.close()