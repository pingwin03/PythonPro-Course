# Zadanie 2 – Walidator wieku
# Stwórz klasę Uzytkownik z atrybutem _wiek. Użyj dekoratora @property, aby stworzyć
# właściwość wiek. Getter powinien zwracać wiek, a setter powinien sprawdzać, czy podany
# wiek jest w zakresie od 0 do 120. Jeśli nie jest, powinien wyświetlić komunikat błędu i nie
# zmieniać wartości.



class Uzytkownik:
    def __init__(self, wiek):
        self._wiek = None
        self.wiek = wiek  # celowo przez setter, żeby walidacja działała od razu

    @property
    def wiek(self):
        return self._wiek

    @wiek.setter
    def wiek(self, wartosc):
        if 0 <= wartosc <= 120:
            self._wiek = wartosc
        else:
            print(f"Błąd: wiek {wartosc} jest poza dopuszczalnym zakresem (0–120). Wartość nie została zmieniona.")


# ── Testy ──────────────────────────────────────────────
u = Uzytkownik(25)
print(f"Wiek po utworzeniu: {u.wiek}")

u.wiek = 30
print(f"Wiek po zmianie na 30: {u.wiek}")

u.wiek = -5
print(f"Wiek po próbie ustawienia -5: {u.wiek}")

u.wiek = 150
print(f"Wiek po próbie ustawienia 150: {u.wiek}")

u.wiek = 0
print(f"Wiek po ustawieniu 0 (granica dolna): {u.wiek}")

u.wiek = 120
print(f"Wiek po ustawieniu 120 (granica górna): {u.wiek}")