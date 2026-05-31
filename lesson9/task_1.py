# Dziennik użytkownika: Napisz program, który w pętli prosi użytkownika o wpisanie jednej
# linii tekstu. Każda wpisana linia powinna być dopisywana (tryb 'a' ) do pliku
# dziennik.txt . Program kończy działanie, gdy użytkownik wpisze "koniec".

while True:
    linia = input("Wpisz tekst (lub 'koniec', aby zakończyć): ")

    if linia == "koniec":
        break

    with open("dziennik.txt", "a", encoding="utf-8") as plik:
        plik.write(linia + "\n")