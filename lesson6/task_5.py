#Adnotacje i docstring: Weź funkcję kalkulator z zadania 1. Dodaj do niej pełne
#adnotacje typów dla wszystkich parametrów i wartości zwracanej. Napisz również
#kompletny docstring opisujący jej działanie.



def kalkulator(a: float, b: float, operacja: str) -> float | str:
    """
    Wykonuje podstawowe działanie matematyczne na dwóch liczbach.

    Funkcja przyjmuje dwie liczby oraz napis określający operację.
    Obsługiwane operacje to:
    "+", "-", "*", "/".

    Args:
        a (float): Pierwsza liczba.
        b (float): Druga liczba.
        operacja (str): Symbol operacji matematycznej.

    Returns:
        float | str: Wynik działania matematycznego albo komunikat o błędzie,
        jeśli operacja jest nieznana lub wystąpi próba dzielenia przez zero.

    Examples:
        kalkulator(2, 3, "+") zwraca 5
        kalkulator(10, 2, "/") zwraca 5.0
    """
    if operacja == "+":
        return a + b
    elif operacja == "-":
        return a - b
    elif operacja == "*":
        return a * b
    elif operacja == "/":
        if b == 0:
            return "Nie można dzielić przez zero"
        return a / b
    else:
        return "Nieznana operacja"