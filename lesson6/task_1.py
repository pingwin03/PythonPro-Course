
def kalkulator(a, b, operacja):
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