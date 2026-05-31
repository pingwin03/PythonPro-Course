# Wyszukiwarka logów: Wyobraź sobie, że masz duży plik log.txt . Napisz program, który
# pyta użytkownika o szukane słowo (np. "ERROR") i zapisuje wszystkie linie zawierające to
# słowo do nowego pliku wyniki_wyszukiwania.txt 


szukane_slowo = input("Podaj szukane słowo: ")

with open("log.txt", "r", encoding="utf-8") as plik_wejsciowy, \
     open("wyniki_wyszukiwania.txt", "w", encoding="utf-8") as plik_wyjsciowy:

    for linia in plik_wejsciowy:
        if szukane_slowo in linia:
            plik_wyjsciowy.write(linia)

print("Zakończono wyszukiwanie. Wyniki zapisano do pliku wyniki_wyszukiwania.txt.")
