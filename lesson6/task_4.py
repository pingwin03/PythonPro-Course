#Sprawdzanie zakresu: Zdefiniuj zmienną globalną POZIOM_DOSTEPU = "user" . Napisz
#funkcję, która próbuje zmienić tę zmienną na "admin" bez użycia słowa kluczowego
#global . Wewnątrz funkcji stwórz zmienną lokalną o tej samej nazwie. Wyświetl wartość
#zmiennej wewnątrz i na zewnątrz funkcji, aby zobaczyć różnicę.


POZIOM_DOSTEPU = "user"

def proba_zmiany():
    POZIOM_DOSTEPU = "admin"  # Tworzy LOKALNĄ zmienną!
    print(f"Wewnątrz funkcji: POZIOM_DOSTEPU = '{POZIOM_DOSTEPU}'")

print(f"Na zewnątrz (przed funkcją): POZIOM_DOSTEPU = '{POZIOM_DOSTEPU}'")
proba_zmiany()
print(f"Na zewnątrz (po funkcji): POZIOM_DOSTEPU = '{POZIOM_DOSTEPU}'")