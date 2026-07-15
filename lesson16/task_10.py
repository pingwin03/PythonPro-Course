# Walidator nagłówków: Napisz funkcję validate_request(request_dict: dict) ,
# która sprawdza, czy w słowniku reprezentującym żądanie HTTP znajdują się kluczowe
# nagłówki: Host i User-Agent .
# Jeśli któregoś z nagłówków brakuje w kluczu headers , funkcja powinna podnieść
# wyjątek ValueError z odpowiednim komunikatem (np. "Brak wymaganego nagłówka:
# Host").
# Użyj bloku try...except , aby przetestować działanie funkcji z poprawnym i
# niepoprawnym słownikiem żądania. To ćwiczenie łączy wiedzę o sieciach z obsługą
# wyjątków.

# Zadanie 10: Walidator nagłówków HTTP z obsługą wyjątków

def validate_request(request_dict: dict):
    # Pobranie słownika nagłówków
    headers = request_dict.get("headers", {})
    
    # Sprawdzenie obecności nagłówka Host
    if "Host" not in headers:
        raise ValueError("Brak wymaganego nagłówka: Host")
        
    # Sprawdzenie obecności nagłówka User-Agent
    if "User-Agent" not in headers:
        raise ValueError("Brak wymaganego nagłówka: User-Agent")
        
    print("Żądanie jest poprawne (posiada wymagane nagłówki).")


# Słowniki testowe
correct_request = {
    "headers": {
        "Host": "mojastrona.pl",
        "User-Agent": "Mozilla/5.0"
    }
}

incorrect_request = {
    "headers": {
        "Host": "mojastrona.pl"
        # Brakuje User-Agent
    }
}

print("Zadanie 10 - Testowanie walidatora:")

# Blok try...except dla poprawnego żądania
try:
    print("Test poprawny:")
    validate_request(correct_request)
except ValueError as e:
    print(f"Wyłapano błąd: {e}")

print("-" * 20)

# Blok try...except dla niepoprawnego żądania
try:
    print("Test niepoprawny:")
    validate_request(incorrect_request)
except ValueError as e:
    print(f"Wyłapano oczekiwany błąd: {e}")