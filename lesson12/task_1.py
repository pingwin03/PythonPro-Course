# Zadanie 1 – Klasa danych Film
# Stwórz klasę danych (@dataclass) o nazwie Film, która będzie przechowywać tytuł (string),
# reżysera (string) i rok_produkcji (integer). Utwórz dwie instancje tej klasy i wyświetl je.


from dataclasses import dataclass

@dataclass
class Film:
    tytul: str
    rezyser: str
    rok_produkcji: int

# Tworzenie dwóch instancji
film1 = Film("P skuła", "Christopher Nolan", 2010)
film2 = Film("Obywatel", "Jonas Poher Rasmussen", 2022)

# Wyświetlanie instancji
print(film1)
print(film2)