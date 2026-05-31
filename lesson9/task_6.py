# Import z CSV: Napisz program, który odczytuje plik produkty.csv i oblicza sumę cen
# wszystkich produktów. Użyj csv.DictReader , aby łatwiej odwoływać się do kolumn po
# nazwach.

import csv

suma_cen = 0.0

with open("produkty.csv", "r", newline="", encoding="utf-8") as plik:
    czytnik = csv.DictReader(plik)
    for wiersz in czytnik:
        suma_cen += float(wiersz["cena"])

print("Suma cen wszystkich produktów:", suma_cen)