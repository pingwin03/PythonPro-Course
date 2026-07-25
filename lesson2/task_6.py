#Wyrażenie logiczne: Napisz program, który pyta, czy użytkownik ma prawo jazdy
#( tak/nie ) i ile ma lat. Wyświetl True , jeśli użytkownik ma 18 lat lub więcej ORAZ ma
#prawo jazdy. W przeciwnym razie wyświetl False .

# Pobranie danych od użytkownika
czy_ma_prawo_jazdy = input("Czy masz prawo jazdy? (tak/nie): ").strip().lower()
wiek = int(input("Ile masz lat?: "))


warunek_prawa_jazdy = czy_ma_prawo_jazdy == "tak"
warunek_wieku = wiek >= 18

# Ostateczny wynik (True, jeśli oba warunki są spełnione, w przeciwnym razie False)
wynik = warunek_wieku and warunek_prawa_jazdy

# Wyświetlenie rezultatu
print(wynik)