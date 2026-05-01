# Bezpieczne pobieranie ze słownika: Napisz funkcję pobierz_wartosc(slownik,
# klucz) , która bezpiecznie zwraca wartość dla danego klucza. Jeśli klucza nie ma, funkcja
# nie powinna rzucać błędu, tylko zwracać None . Zrób to bez użycia try...except
# (wskazówka: metoda .get() ). Następnie napisz drugą wersję z użyciem try...except
# KeyError 

def pobierz_wartosc(slownik, klucz):
    return slownik.get(klucz)





#druga wersja

def pobierz_wartosc_try(slownik, klucz):
    try:
        return slownik[klucz]
    except KeyError:
        return None
    
    
    dane = {"imie": "Anna", "wiek": 30}

print(pobierz_wartosc(dane, "imie"))   # Anna
print(pobierz_wartosc(dane, "miasto"))  # None

print(pobierz_wartosc_try(dane, "wiek"))   # 30
print(pobierz_wartosc_try(dane, "adres"))  # None