# Zadanie 9 – Klasa KontoBankowe z property i wyjątkami
# Stwórz klasę KontoBankowe za pomocą @dataclass, która ma atrybut _saldo (prywatne).
# Stwórz właściwość ( @property ) saldo , która tylko odczytuje wartość _saldo .
# Stwórz metodę wplac(kwota) , która dodaje kwotę do salda. Metoda powinna podnosić
# ValueError , jeśli kwota jest ujemna.
# Stwórz metodę wyplac(kwota) , która odejmuje kwotę od salda. Metoda powinna
# podnosić ValueError , jeśli kwota do wypłaty jest ujemna, oraz własny wyjątek
# BrakSrodkowError , jeśli saldo jest niewystarczające.
# Przetestuj działanie klasy, obsługując wszystkie możliwe wyjątki.


from dataclasses import dataclass

class BrakSrodkowError(Exception):
    pass


@dataclass
class KontoBankowe:
    _saldo: float

    @property
    def saldo(self):
        return self._saldo

    def wplac(self, kwota):
        if kwota < 0:
            raise ValueError("Kwota wpłaty nie może być ujemna.")
        self._saldo += kwota

    def wyplac(self, kwota):
        if kwota < 0:
            raise ValueError("Kwota wypłaty nie może być ujemna.")
        if kwota > self._saldo:
            raise BrakSrodkowError("Brak wystarczających środków na koncie.")
        self._saldo -= kwota


# Test działania
konto = KontoBankowe(1000)

print("Stan początkowy:", konto.saldo)

try:
    konto.wplac(500)
    print("Po wpłacie 500:", konto.saldo)
except ValueError as e:
    print("Błąd wpłaty:", e)

try:
    konto.wyplac(300)
    print("Po wypłacie 300:", konto.saldo)
except ValueError as e:
    print("Błąd wypłaty:", e)
except BrakSrodkowError as e:
    print("Błąd:", e)

try:
    konto.wplac(-50)
except ValueError as e:
    print("Błąd wpłaty:", e)

try:
    konto.wyplac(-20)
except ValueError as e:
    print("Błąd wypłaty:", e)
except BrakSrodkowError as e:
    print("Błąd:", e)

try:
    konto.wyplac(5000)
except ValueError as e:
    print("Błąd wypłaty:", e)
except BrakSrodkowError as e:
    print("Błąd:", e)

print("Stan końcowy:", konto.saldo)