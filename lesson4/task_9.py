x = 10
print(f"id(x) = {id(x)}")
x += 1  # x = x + 1
print(f"id(x) = {id(x)}")

# Identifikator (id) się ZMIENIA.


# - W Pythonie liczby całkowite (int) są NIEMUTOWALNE (immutable).
# - Operacja x = x + 1 nie zmienia wartości obiektu 10 — zamiast tego tworzy NOWY obiekt (11).
# - Zmienna x zostaje następnie przypisana do tego nowego obiektu, więc jej id() zmienia się na id obiektu 11.
# - Jeśli x był 10 (id = np. 140234567890), po x = x + 1 x wskazuje na 11 (id = np. 140234568010).
#
# Podsumowanie:
# - id(x) przed zmianą ≠ id(x) po zmianie
# - Zmiana wartości liczby całkowitej = nowy obiekt = nowy identyfikator.
