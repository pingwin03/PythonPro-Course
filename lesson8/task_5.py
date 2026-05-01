# Logowanie błędów: Zmodyfikuj zadanie 1. tak, aby każdy napotkany wyjątek (wraz z jego
# treścią) był zapisywany do pliku log.txt , a program kontynuował działanie. Użyj bloku
# finally , aby upewnić się, że plik z logami jest zawsze zamykany.
while True:
    log_plik = None

    try:
        log_plik = open("log.txt", "a", encoding="utf-8")

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
            raise ValueError("Nieznana operacja.")

    except Exception as e:
        print("Wystąpił błąd:", e)
        if log_plik is not None:
            log_plik.write(f"{type(e).__name__}: {e}\n")

    else:
        print("Wynik:", wynik)

    finally:
        if log_plik is not None:
            log_plik.close()
        print("Kolejna operacja...")