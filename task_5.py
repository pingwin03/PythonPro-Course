# Zadanie 5 – Polimorficzna Figura
# Stwórz klasę bazową Figura z metodą oblicz_pole(), która pass (nic nie robi). Następnie
# stwórz dwie klasy potomne: Kwadrat (z atrybutem bok) i Kolo (z atrybutem promien). W obu
# klasach nadpisz metodę oblicz_pole() odpowiednimi wzorami matematycznymi (dla koła
# przyjmij PI=3.14159). Stwórz listę zawierającą jeden kwadrat i jedno koło, a następnie w
# pętli wydrukuj pole każdej figury








class Figura:
    def oblicz_pole(self):
        pass


class Kwadrat(Figura):
    def __init__(self, bok):
        self.bok = bok

    def oblicz_pole(self):
        return self.bok ** 2


class Kolo(Figura):
    PI = 3.14159

    def __init__(self, promien):
        self.promien = promien

    def oblicz_pole(self):
        return self.PI * self.promien ** 2


# Lista zawierająca różne figury
figury = [
    Kwadrat(5),
    Kolo(3)
]

# Pętla – polimorfizm w akcji
for figura in figury:
    print(f"{figura.__class__.__name__}: pole = {figura.oblicz_pole()}")