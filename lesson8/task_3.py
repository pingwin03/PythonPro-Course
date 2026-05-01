# Czytanie pliku: Napisz funkcję, która próbuje otworzyć i odczytać plik o podanej nazwie.
# Obsłuż wyjątki FileNotFoundError (gdy pliku nie ma) oraz PermissionError (gdy nie
# ma uprawnień do odczytu)

def czytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            tresc = plik.read()
            return tresc

    except FileNotFoundError:
        print("Błąd: plik nie istnieje.")

    except PermissionError:
        print("Błąd: brak uprawnień do odczytu pliku.")


nazwa = input("Podaj nazwę pliku: ")
wynik = czytaj_plik(nazwa)

if wynik is not None:
    print("Zawartość pliku:")
    print(wynik)