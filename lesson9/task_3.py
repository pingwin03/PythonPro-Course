# Konfiguracja w JSON: Stwórz słownik Pythona z ustawieniami aplikacji, np.
# konfiguracja = {"uzytkownik": "admin", "motyw": "ciemny", "rozdzielczosc":
# [1920, 1080]} . Zapisz ten słownik do pliku config.json z wcięciami i poprawnym
# kodowaniem polskich znaków

import json

konfiguracja = {
    "uzytkownik": "admin",
    "motyw": "ciemny",
    "rozdzielczosc": [1920, 1080]
}

with open("config.json", "w", encoding="utf-8") as plik:
    json.dump(konfiguracja, plik, indent=4, ensure_ascii=False)