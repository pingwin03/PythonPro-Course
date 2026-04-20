sekret = 42

while True:
    liczba = int(input("Zgadnij liczbę: "))

    if liczba == sekret:
        print("Gratulacje! Odgadłeś liczbę!")
        break
    else:
        print("To zła liczba, spróbuj ponownie.")