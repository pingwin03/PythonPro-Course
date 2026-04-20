#Tworzenie profilu: Napisz funkcję stworz_profil(imie, **dane_dodatkowe) , która
#przyjmuje imię oraz dowolną liczbę nazwanych argumentów (np. wiek=30 ,
#miasto="Warszawa" ). Funkcja powinna zwrócić słownik z profilem użytkownika, gdzie
#klucz 'imie' jest obowiązkowy, a reszta danych jest pobierana z **dane_dodatkowe 


def stworz_profil(imie, **dane_dodatkowe):
    profil = {"imie": imie}
    profil.update(dane_dodatkowe)
    return profil


profil1 = stworz_profil("Rafał", wiek=44, miasto="Warszawa")
profil2 = stworz_profil("Monika", zawod="Programista", hobby="hulajnoga")

print(profil1)
print(profil2)