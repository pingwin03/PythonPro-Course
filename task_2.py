# Zadanie 2 – Atrybuty Produkt
# Zdefiniuj klasę Produkt z konstruktorem init przyjmującym nazwa, cena i kategoria. Stwórz
# obiekt tej klasy, a następnie wydrukuj każdy z jego atrybutów w osobnej linii.


class Produkt:
    def __init__(self, nazwa, cena, kategoria):
        self.nazwa = nazwa
        self.cena = cena
        self.kategoria = kategoria


# Tworzę obiekt klasy Produkt
produkt = Produkt("Laptop", 3499.99, "Elektronika")

# Drukuję każdy atrybut w osobnej linii
print(produkt.nazwa)
print(produkt.cena)
print(produkt.kategoria)