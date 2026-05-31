# Eksport do CSV: Masz listę słowników: produkty = [{"nazwa": "Mleko", "cena":
# 3.50}, {"nazwa": "Chleb", "cena": 4.20}] . Zapisz te dane do pliku produkty.csv ,
# gdzie pierwszy wiersz to nagłówki ("nazwa", "cena").


import csv

produkty = [
    {"nazwa": "Mleko", "cena": 3.50},
    {"nazwa": "Chleb", "cena": 4.20}
]

with open("produkty.csv", "w", newline="", encoding="utf-8") as plik:
    pisarz = csv.DictWriter(plik, fieldnames=["nazwa", "cena"])
    pisarz.writeheader()
    pisarz.writerows(produkty)