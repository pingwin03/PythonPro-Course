# Zadanie 1 – Klasa Film
# Zadania z gwiazdką (challenge)
# Stwórz klasę Film, która przy tworzeniu obiektu będzie przyjmować tytul, rezyser i
# rok_produkcji. Dodaj metodę informacje(), która będzie zwracać string z pełnymi
# informacjami o filmie w formacie: "Tytuł" (rok_produkcji), reżyseria: Reżyser. Stwórz dwa
# obiekty tej klasy i wydrukuj informacje o nich.

class Film:
    def __init__(self, tytul, rezyser, rok_produkcji):
        self.tytul = tytul
        self.rezyser = rezyser
        self.rok_produkcji = rok_produkcji

    def informacje(self):
        return f'"{self.tytul}" ({self.rok_produkcji}), reżyseria: {self.rezyser}'


# Tworzymy dwa obiekty klasy Film
film1 = Film("Skazani na Shawshank", "Frank Darabont", 1994)
film2 = Film("Inception", "Christopher Nolan", 2010)

# Drukujemy informacje o filmach
print(film1.informacje())
print(film2.informacje())
