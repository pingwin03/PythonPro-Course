sekret = 42

while True:
    try:
        liczba = int(input("Podaj liczbę: "))
    except ValueError:
        print("Błąd: wpisz poprawną liczbę całkowitą.")
        continue

    if liczba == sekret:
        print("Gratulacje! Odgadłeś liczbę!")
        break
    else:
        print("Zła liczba, spróbuj jeszcze raz.")
