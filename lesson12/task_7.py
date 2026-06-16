# Zadanie 7 – Alternatywny konstruktor dla Daty
# Stwórz klasę Data z atrybutami dzien, miesiac, rok. Dodaj metodę klasy (@classmethod) o
# nazwie ze_stringa, która przyjmuje datę w formacie "DD-MM-RRRR" (np. "25-12-2023") i
# tworzy na jej podstawie obiekt klasy Data. Pamiętaj o konwersji typów na int.


class Data:
    def __init__(self, dzien, miesiac, rok):
        self.dzien = dzien
        self.miesiac = miesiac
        self.rok = rok

    @classmethod
    def ze_stringa(cls, data_string):
        """Alternatywny konstruktor: tworzy Data z 'DD-MM-RRRR'."""
        dzien, miesiac, rok = map(int, data_string.split("-"))
        return cls(dzien, miesiac, rok)

    def __str__(self):
        return f"{self.dzien:02d}-{self.miesiac:02d}-{self.rok}"


# Test działania
data1 = Data(25, 12, 2023)
print("Data z konstruktora:", data1)

data2 = Data.ze_stringa("25-12-2023")
print("Data ze_stringa:", data2)

data3 = Data.ze_stringa("1-1-2026")
print("Kolejna data:", data3)