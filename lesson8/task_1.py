# Bezpieczny kalkulator: Napisz program, który w pętli prosi użytkownika o podanie dwóch
# liczb i operacji ( + , - , * , / ). Zaimplementuj pełną obsługę błędów ValueError (gdy
# dane nie są liczbami) i ZeroDivisionError . Dodaj blok else do wyświetlania wyniku i
# finally z komunikatem "Kolejna operacja...".

while True:
    try:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        operacja = input("Podaj operację (+, -, *, /): ")

        if operacja == "+":
            wynik = a + b
        elif operacja == "-":
            wynik = a - b
        elif operacja == "*":
            wynik = a * b
        elif operacja == "/":
            wynik = a / b
        else:
            print("Nieznana operacja.")
            continue

    except ValueError:
        print("Błąd: musisz podać poprawne liczby.")

    except ZeroDivisionError:
        print("Błąd: nie można dzielić przez zero.")

    else:
        print("Wynik:", wynik)

    finally:
        print("Kolejna operacja...")