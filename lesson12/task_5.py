# Zadanie 5 – Odczyt pliku
# Napisz program, który próbuje otworzyć i odczytać plik o nazwie nieistniejacy.txt. Użyj bloku
# try...except, aby obsłużyć wyjątek FileNotFoundError i wyświetlić przyjazny komunikat
# użytkownikowi.


try:
    with open("nieistniejacy.txt", "r", encoding="utf-8") as plik:
        zawartosc = plik.read()
        print(zawartosc)
except FileNotFoundError:
    print("Błąd: Plik 'nieistniejacy.txt' nie został znaleziony.")
    print("Sprawdź, czy plik istnieje i czy podałeś poprawną nazwę.")