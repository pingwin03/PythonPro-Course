#Kalkulator zniżek: Napisz program, który oblicza cenę biletu. Cena bazowa to 100 PLN.
#Jeśli użytkownik jest studentem ( tak/nie ) LUB ma mniej niż 18 lat, przysługuje mu 50%
#zniżki. Użyj operatorów or i and .
cena_bazowa = 100

wiek = int(input("Podaj swój wiek: "))
student = input("Czy jesteś studentem? (tak/nie): ").lower()

if (student == "tak" or wiek < 18) and wiek >= 0:
    cena = cena_bazowa * 0.5
else:
    cena = cena_bazowa

print("Cena biletu wynosi:", cena, "PLN")
