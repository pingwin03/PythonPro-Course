#Analiza wieku: Napisz program, który pobiera od użytkownika wiek. Używając instrukcji
#if-elif-else , wyświetl jeden z komunikatów: "Niemowlę" (0-1), "Dziecko" (2-12),
#"Nastolatek" (13-17), "Dorosły" (18-64), "Senior" (65+).


while True:
    try:
        wiek = int(input("Podaj wiek: "))
    except ValueError:
        print("Błąd: wpisz poprawną liczbę całkowitą.")
        continue

    if wiek < 0:
        print("Błąd: wiek nie może być ujemny.")
    elif wiek <= 1:
        print("Niemowlę")
        break
    elif wiek <= 12:
        print("Dziecko")
        break
    elif wiek <= 17:
        print("Nastolatek")
        break
    elif wiek <= 64:
        print("Dorosły")
        break
    else:
        print("Senior")
        break
