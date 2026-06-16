# Zadanie 10 – Metaklasa walidująca
# Stwórz metaklasę MetaWalidujMetody, która podczas tworzenia nowej klasy sprawdza, czy
# wszystkie jej metody (poza metodami "magicznymi", czyli zaczynającymi się od __) mają
# docstring. Jeśli któraś metoda go nie ma, metaklasa powinna podnieść TypeError z
# informacją, która metoda wymaga dokumentacji. Przetestuj ją, tworząc klasę z poprawnie i
# niepoprawnie udokumentowanymi metodami.


import inspect


class MetaWalidujMetody(type):
    def __new__(mcs, nazwa, rodzice, atrybuty):
        for klucz, wartosc in atrybuty.items():
            if callable(wartosc) and not klucz.startswith("__"):
                if not inspect.getdoc(wartosc):
                    raise TypeError(
                        f"Metoda '{klucz}' w klasie '{nazwa}' nie ma docstringa. "
                        f"Dodaj dokumentację!"
                    )
        return super().__new__(mcs, nazwa, rodzice, atrybuty)


# ── Test 1: klasa poprawnie udokumentowana ──────────────
print("Tworzenie klasy PoprawnaKlasa...")

class PoprawnaKlasa(metaclass=MetaWalidujMetody):
    def dodaj(self, a, b):
        """Zwraca sumę dwóch liczb."""
        return a + b

    def powitaj(self, imie):
        """Wyświetla powitanie dla podanego imienia."""
        print(f"Cześć, {imie}!")

print("✅ PoprawnaKlasa utworzona pomyślnie.\n")


# ── Test 2: klasa z brakującym docstringiem ─────────────
print("Tworzenie klasy NiepoprawnaKlasa...")

try:
    class NiepoprawnaKlasa(metaclass=MetaWalidujMetody):
        def udokumentowana(self):
            """Ta metoda ma docstring."""
            pass

        def bez_dokumentacji(self):
            pass

except TypeError as e:
    print(f"❌ TypeError: {e}\n")


# ── Test 3: metody magiczne są pomijane ─────────────────
print("Tworzenie klasy ZMagicznymi (metody __init__, __str__ bez docstringa)...")

class ZMagicznymi(metaclass=MetaWalidujMetody):
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"ZMagicznymi({self.x})"

    def oblicz(self):
        """Zwraca wartość x pomnożoną przez 2."""
        return self.x * 2

print("✅ ZMagicznymi utworzona pomyślnie – metody magiczne są pomijane.")