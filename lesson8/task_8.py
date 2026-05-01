# Walidacja hasła v2: Rozbuduj funkcję do walidacji hasła. Powinna ona zwracać listę
# wszystkich błędów walidacji, zamiast rzucać wyjątkiem po pierwszym napotkanym
# problemie. Jeśli lista błędów nie jest pusta, rzuć własnym wyjątkiem BladWalidacjiError ,
# przekazując do niego tę listę.

class BladWalidacjiError(Exception):
    def __init__(self, bledy):
        self.bledy = bledy
        super().__init__("Wystąpiły błędy walidacji.")


def waliduj_haslo(haslo):
    bledy = []

    if len(haslo) < 8:
        bledy.append("Hasło musi mieć co najmniej 8 znaków.")

    if not any(znak.isupper() for znak in haslo):
        bledy.append("Hasło musi zawierać co najmniej jedną wielką literę.")

    if not any(znak.islower() for znak in haslo):
        bledy.append("Hasło musi zawierać co najmniej jedną małą literę.")

    if not any(znak.isdigit() for znak in haslo):
        bledy.append("Hasło musi zawierać co najmniej jedną cyfrę.")

    if not any(not znak.isalnum() for znak in haslo):
        bledy.append("Hasło musi zawierać co najmniej jeden znak specjalny.")

    if bledy:
        raise BladWalidacjiError(bledy)

    return "Hasło jest poprawne."


try:
    wynik = waliduj_haslo("abc")
    print(wynik)

except BladWalidacjiError as e:
    print("Błędy walidacji:")
    for blad in e.bledy:
        print("-", blad)