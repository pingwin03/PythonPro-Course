# Zadanie 6 – Własny wyjątek InvalidPasswordError
# Stwórz własny wyjątek InvalidPasswordError. Następnie napisz funkcję ustaw_haslo(haslo),
# która sprawdza, czy hasło ma co najmniej 8 znaków. Jeśli nie, funkcja powinna podnieść
# (raise) wyjątek InvalidPasswordError z odpowiednim komunikatem. Napisz kod, który
# testuje tę funkcję w bloku try...except



class InvalidPasswordError(Exception):
    pass


def ustaw_haslo(haslo):
    if len(haslo) < 8:
        raise InvalidPasswordError(
            f"Hasło za krótkie: ma {len(haslo)} znaki/znaków, wymagane minimum 8."
        )
    return haslo


# ── Testy ──────────────────────────────────────────────
hasla = ["abc", "", "poprawneHaslo123", "1234567", "dokładnie"]

for haslo in hasla:
    try:
        wynik = ustaw_haslo(haslo)
        print(f"✅ Hasło '{wynik}' zostało ustawione.")
    except InvalidPasswordError as e:
        print(f"❌ {e}")