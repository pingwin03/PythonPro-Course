#Mini-projekt: Walidator hasła: Stwórz funkcję sprawdz_haslo(haslo: str) -> bool .
#Funkcja powinna sprawdzać, czy hasło spełnia następujące warunki i zwracać True lub
#False :
#Ma co najmniej 8 znaków.
#Zawiera co najmniej jedną wielką literę.
#Zawiera co najmniej jedną cyfrę. Napisz do niej pełną dokumentację (docstring i
#adnotacje)

def sprawdz_haslo(haslo: str) -> bool:
    if len(haslo) < 8:
        return False
    if not any(znak.isupper() for znak in haslo):
        return False
    if not any(znak.isdigit() for znak in haslo):
        return False
    return True

#wpisując sprawdza nam warunki
print(sprawdz_haslo("Haslo123"))   # True
print(sprawdz_haslo("haslo123"))   # False
print(sprawdz_haslo("Haslo"))      # False