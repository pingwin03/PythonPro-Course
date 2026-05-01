# Kontekstowy menedżer with : Pokaż, jak instrukcja with open(...) as f: upraszcza
# kod z zadania 3, eliminując potrzebę jawnego używania bloku finally do zamykania
# pliku.

def czytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            return plik.read()
    except FileNotFoundError:
        print("Błąd: plik nie istnieje.")
    except PermissionError:
        print("Błąd: brak uprawnień do odczytu.")
        
zawartosc = czytaj_plik("dane.txt")
if zawartosc is not None:
    print(zawartosc)