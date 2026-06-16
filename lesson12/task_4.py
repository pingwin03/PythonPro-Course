# Zadanie 4 – Bezpieczne dzielenie
# Napisz funkcję bezpieczne_dzielenie(a, b), która zwraca wynik dzielenia a / b. Użyj bloku
# try...except, aby obsłużyć błąd ZeroDivisionError. Jeśli wystąpi ten błąd, funkcja powinna
# zwrócić None i wyświetlić komunikat "Błąd: Dzielenie przez zero!"



def bezpieczne_dzielenie(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Błąd: Dzielenie przez zero!")
        return None


# Test działania
print(bezpieczne_dzielenie(10, 2))   # poprawne: 5.0
print(bezpieczne_dzielenie(10, 0))   # błąd: None + komunikat
print(bezpieczne_dzielenie(5, 0))    # kolejny błąd