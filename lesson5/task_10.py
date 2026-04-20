#Mini-projekt: Prosty kalkulator walut:
#Zdefiniuj kursy w słowniku, np. kursy = {"USD": 4.0, "EUR": 4.3} .
#W pętli while True zapytaj użytkownika o kwotę w PLN i walutę (USD/EUR).
#Użyj if-elif-else , aby sprawdzić wybraną walutę i obliczyć wynik.
#Sformatuj wynik do dwóch miejsc po przecinku, używając f-stringa.
#Zapytaj użytkownika, czy chce kontynuować. Jeśli odpowie "nie", użyj break 




kursy = {"USD": 4.0, "EUR": 4.3}

while True:
    kwota_pln = float(input("Podaj kwotę w PLN: "))
    waluta = input("Podaj walutę (USD/EUR): ").upper()

    if waluta == "USD":
        wynik = kwota_pln / kursy["USD"]
        print(f"Otrzymasz {wynik:.2f} USD")
    elif waluta == "EUR":
        wynik = kwota_pln / kursy["EUR"]
        print(f"Otrzymasz {wynik:.2f} EUR")
    else:
        print("Nieznana waluta.")

    dalej = input("Czy chcesz kontynuować? (tak/nie): ").lower()

    if dalej == "nie":
        print("Koniec programu.")
        break