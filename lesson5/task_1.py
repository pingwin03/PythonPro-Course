#Analiza wieku: Napisz program, który pobiera od użytkownika wiek. Używając instrukcji
#if-elif-else , wyświetl jeden z komunikatów: "Niemowlę" (0-1), "Dziecko" (2-12),
#"Nastolatek" (13-17), "Dorosły" (18-64), "Senior" (65+).


wiek = int(input("Podaj swój wiek: "))

if wiek >= 0 and wiek <= 1:
    print("Niemowlę")
elif wiek >= 2 and wiek <= 12:
    print("Dziecko")
elif wiek >= 13 and wiek <= 17:
    print("Nastolatek")
elif wiek >= 18 and wiek <= 64:
    print("Dorosły")
elif wiek >= 65:
    print("Senior")
else:
    print("Podano nieprawidłowy wiek")