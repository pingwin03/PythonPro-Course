# Zadanie 8 – Hierarchia instrumentów muzycznych
# Zaprojektuj hierarchię klas: Instrument -> Strunowy i Dety. Następnie Gitara (dziedziczy po
# Strunowy) i Trabka (dziedziczy po Dety). Klasa Instrument powinna mieć metodę graj(),
# która zwraca ogólny komunikat. Każda kolejna klasa w hierarchii powinna nadpisywać tę
# metodę, dodając coś od siebie i wywołując wersję z klasy nadrzędnej za pomocą
# super().graj().
# Instrument.graj() -> "Wydaje dźwięk."
# Strunowy.graj() -> "Wydaje dźwięk. [Szarpnięcie struny]"
# Gitara.graj() -> "Wydaje dźwięk. [Szarpnięcie struny] [Akord G-dur]"


class Instrument:
    def graj(self):
        return "Wydaje dźwięk."


class Strunowy(Instrument):
    def graj(self):
        return super().graj() + " [Szarpnięcie struny]"


class Dety(Instrument):
    def graj(self):
        return super().graj() + " [Dmuchnięcie w ustnik]"


class Gitara(Strunowy):
    def graj(self):
        return super().graj() + " [Akord G-dur]"


class Trabka(Dety):
    def graj(self):
        return super().graj() + " [Fanfara C-dur]"


# Tworzymy obiekty i testujemy
instrumenty = [
    Instrument(),
    Strunowy(),
    Dety(),
    Gitara(),
    Trabka(),
]

for instrument in instrumenty:
    nazwa = instrument.__class__.__name__
    print(f"{nazwa:10} -> {instrument.graj()}")