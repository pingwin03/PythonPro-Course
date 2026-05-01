# Mini-projekt: Przetwarzanie danych: Masz listę słowników reprezentujących
# użytkowników:
# uzytkownicy = [
# {"imie": "Jan", "wiek": 30, "aktywny": True},
# {"imie": "Anna", "wiek": 17, "aktywny": False},
# {"imie": "Piotr", "wiek": 25, "aktywny": True}
# ]
# Napisz jednolinijkowy kod (używając kombinacji filter , map lub list comprehension),
# który zwróci listę imion aktywnych użytkowników, którzy mają 18 lat lub więcej, pisanych
# wielkimi literami.

uzytkownicy = [
    {"imie": "Jan", "wiek": 30, "aktywny": True},
    {"imie": "Anna", "wiek": 17, "aktywny": False},
    {"imie": "Piotr", "wiek": 25, "aktywny": True}
]

wynik = [u["imie"].upper() for u in uzytkownicy if u["aktywny"] and u["wiek"] >= 18]

print(wynik)