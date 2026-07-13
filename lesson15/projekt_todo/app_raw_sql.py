# app_raw_sql.py
import database_raw as db

def pokaz_zadania():
    """Wyświetla listę wszystkich zadań."""
    zadania = db.pobierz_zadania()
    if not zadania:
        print("Brak zadań na liście.")
        return
    print("\n--- Twoja lista zadań ---")
    for zadanie in zadania:
        status = "v" if zadanie[2] else "x"
        print(f"[{status}] ID: {zadanie[0]}, Opis: {zadanie[1]}")
    print("\n")

# Zadanie 1 – Usuwanie zadań (Raw SQL)
# Dodaj do aplikacji app_raw_sql.py opcję menu "Usuń zadanie". Zaimplementuj funkcję
# usun_zadanie(id_zadania) w database_raw.py, która użyje zapytania DELETE FROM
# zadania WHERE id = ?

# i dodatkowo:
#     Zadanie 3 – Wyświetlanie ID
# Zmodyfikuj funkcję pokaz_zadania w obu aplikacjach tak, aby oprócz opisu i statusu,
# wyświetlała również ID każdego zadania. (W wersji ORM już to zrobiliśmy, upewnij się, że
# wiesz dlaczego to działa).

# Zadanie 6 – Wyszukiwanie po opisie (Raw SQL)
# Dodaj do aplikacji app_raw_sql.py funkcję wyszukiwania zadań. Użytkownik podaje frazę, a
# program wyświetla wszystkie zadania, których opis zawiera tę frazę. Użyj operatora LIKE i
# wzorca %fraza% w zapytaniu SELECT.

def main():
    db.init_db()
    while True:
        print("Menu:")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz zadanie jako zrobione")
        print("4. Usuń zadanie")  # <--- Nowa opcja
        print("5. Wyszukaj zadanie")
        print("6. Wyjdź")
        wybor = input("Wybierz opcję: ")
        
        if wybor == '1':
            pokaz_zadania()
        elif wybor == '2':
            opis = input("Podaj opis zadania: ")
            db.dodaj_zadanie(opis)
            print("Zadanie dodane!")
        elif wybor == '3':
            try:
                id_zadania = int(input("Podaj ID zadania do oznaczenia: "))
                db.oznacz_jako_zrobione(id_zadania)
                print("Zadanie zaktualizowane!")
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == '4':  # <--- Obsługa usuwania
            try:
                id_zadania = int(input("Podaj ID zadania do usunięcia: "))
                db.usun_zadanie(id_zadania)
                print("Zadanie usunięte!")
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
     
        if wybor == '5':
            fraza = input("Podaj szukaną frazę: ")
            zadania = db.szukaj_zadania(fraza)
            if not zadania:
                print("Nie znaleziono zadań pasujących do frazy.")
            else:
                print("\n--- Wyniki wyszukiwania ---")
                for zadanie in zadania:
                    status = "v" if zadanie[2] else "x"
                    print(f"[{status}] ID: {zadanie[0]}, Opis: {zadanie[1]}")
        elif wybor == '6':
            break

if __name__ == "__main__":
    main()