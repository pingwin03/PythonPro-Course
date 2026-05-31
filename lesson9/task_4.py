# Odczyt konfiguracji: Napisz program, który odczytuje plik config.json z poprzedniego
# zadania i wyświetla komunikat: Witaj, [uzytkownik]! Twój motyw to [motyw].


import json

with open("config.json", "r", encoding="utf-8") as plik:
    konfiguracja = json.load(plik)

print(f"Witaj, {konfiguracja['uzytkownik']}! Twój motyw to {konfiguracja['motyw']}.")