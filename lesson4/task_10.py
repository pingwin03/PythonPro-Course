def oblicz_pole_prostokata(a, b):
    """
    Oblicza pole prostokąta o bokach a i b.

    Parametry:
        a (int lub float): długość pierwszego boku prostokąta.
        b (int lub float): długość drugiego boku prostokąta.

    Zwraca:
        int lub float: pole prostokąta, obliczone jako a * b.
    """
    # Obliczamy pole prostokąta jako iloczyn długości boków a i b.
    pole = a * b
    # Zwracamy obliczone pole jako wynik funkcji.
    return pole

# Długość pierwszego boku prostokąta.
bok_a = 10

# Długość drugiego boku prostokąta.
bok_b = 20

# Wywołujemy funkcję oblicz_pole_prostokata z bokami bok_a i bok_b.
wynik = oblicz_pole_prostokata(bok_a, bok_b)

# Wyświetlamy wynik w czytelnej formie, używając formatowania f-string.
print(f"Pole prostokąta o bokach {bok_a} i {bok_b} wynosi {wynik}.")
