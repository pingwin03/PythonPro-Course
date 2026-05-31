# Mini-projekt: Lista zadań: Stwórz prostą aplikację do zarządzania listą zadań. Program
# powinien:
# Przy starcie próbować wczytać zadania z pliku zadania.json .
# Pozwalać użytkownikowi dodać nowe zadanie.
# Pozwalać wyświetlić wszystkie zadania.
# Przy zamknięciu (lub na polecenie) zapisywać aktualną listę zadań do pliku
# zadania.json .

import json

PLIK = "zadania.json"


def wczytaj_zadania():
    try:
        with open(PLIK, "r", encoding="utf-8") as plik:
            return json.load(plik)
    except FileNotFoundError:
        return []


def zapisz_zadania(zadania):
    with open(PLIK, "w", encoding="utf-8") as plik:
        json.dump(zadania, plik, indent=4, ensure_ascii=False)


def pokaz_zadania(zadania):
    if not zadania:
        print("Lista zadań jest pusta.")
    else:
        print("\nTwoje zadania:")
        for nr, zadanie in enumerate(zadania, start=1):
            print(f"{nr}. {zadanie}")


def main():
    zadania = wczytaj_zadania()

    while True:
        print("\n--- MENU ---")
        print("1. Dodaj zadanie")
        print("2. Wyświetl zadania")
        print("3. Zapisz i zakończ")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            nowe_zadanie = input("Podaj treść zadania: ")
            zadania.append(nowe_zadanie)
            print("Dodano zadanie.")

        elif wybor == "2":
            pokaz_zadania(zadania)

        elif wybor == "3":
            zapisz_zadania(zadania)
            print("Zadania zapisano do pliku. Koniec programu.")
            break

        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")


main()