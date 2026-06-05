# Zadanie 9 – Walidacja danych w init
# Stwórz klasę RejestracjaUzytkownika. W konstruktorze init przyjmuj email i haslo.
# Wewnątrz konstruktora dodaj walidację:
# Sprawdź, czy email zawiera znak @ . Jeśli nie, podnieś wyjątek ValueError z
# odpowiednim komunikatem.
# Sprawdź, czy haslo ma co najmniej 8 znaków. Jeśli nie, podnieś ValueError. Użyj bloku
# try...except, aby przetestować tworzenie obiektów z poprawnymi i niepoprawnymi
# danymi.



class RejestracjaUzytkownika:
    def __init__(self, email, haslo):
        if "@" not in email:
            raise ValueError(f"Nieprawidłowy email: '{email}' – brak znaku '@'.")
        if len(haslo) < 8:
            raise ValueError(f"Hasło za krótkie – minimum 8 znaków (podano {len(haslo)}).")

        self.email = email
        self.haslo = haslo

    def __str__(self):
        return f"Użytkownik: {self.email} (hasło: {'*' * len(self.haslo)})"


# ── Testy ──────────────────────────────────────────────
przypadki = [
    ("jan.kowalski@example.com", "bezpieczneHaslo123"),  # ✅ poprawne
    ("nieprawidlowy-email",      "bezpieczneHaslo123"),  # ❌ brak @
    ("anna@example.com",         "kr0t"),                # ❌ hasło za krótkie
    ("",                         ""),                    # ❌ oba błędy
]

for email, haslo in przypadki:
    print(f"Próba rejestracji: email='{email}', hasło='{haslo}'")
    try:
        user = RejestracjaUzytkownika(email, haslo)
        print(f"  ✅ Sukces! {user}")
    except ValueError as e:
        print(f"  ❌ Błąd: {e}")
    print()