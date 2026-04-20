imiona = ["Anna", "Jan", "Piotr", "Kasia"]

szukane = input("Podaj imię do wyszukania: ")

for imie in imiona:
    if imie == szukane:
        print("Znaleziono!")
        break
else:
    print("Nie znaleziono imienia na liście.")