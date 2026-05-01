# Przerzucanie wyjątku: Napisz funkcję przetworz_dane(dane) , która w bloku
# try...except łapie KeyError (np. przy próbie dostępu do nieistniejącego klucza w
# słowniku), loguje go, a następnie rzuca ( raise ) nowy, własny wyjątek
# BladPrzetwarzaniaDanychError z informacją, którego klucza brakowało

class BladPrzetwarzaniaDanychError(Exception):
    pass
def przetworz_dane(dane):
    try:
        imie = dane["imie"]
        wiek = dane["wiek"]
        print(f"Przetwarzam użytkownika: {imie}, wiek: {wiek}")

    except KeyError as e:
        brakujacy_klucz = e.args[0]

        with open("log.txt", "a", encoding="utf-8") as log:
            log.write(f"KeyError: brakuje klucza '{brakujacy_klucz}'\n")

        raise BladPrzetwarzaniaDanychError(
            f"Nie można przetworzyć danych - brakuje klucza: {brakujacy_klucz}"
        ) from e


try:
    dane = {"imie": "Anna"}
    przetworz_dane(dane)

except BladPrzetwarzaniaDanychError as e:
    print("Własny wyjątek:", e)