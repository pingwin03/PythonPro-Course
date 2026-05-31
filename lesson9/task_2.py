# Licznik słów: Stwórz program, który pyta o nazwę pliku, odczytuje go, a następnie zlicza i
# wyświetla całkowitą liczbę słów w tym pliku. Obsłuż błąd FileNotFoundError , jeśli plik nie
# istnieje.

nazwa_pliku = input("Podaj nazwę pliku: ")
try:
    with open(nazwa_pliku, "r", encoding="utf-8") as plik:
        tresc = plik.read()
        liczba_slow = len(tresc.split())
        print("Liczba słów w pliku:", liczba_slow)

except FileNotFoundError:
    print("Błąd: podany plik nie istnieje.")