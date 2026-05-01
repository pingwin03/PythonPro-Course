#Znajdowanie liczb pierwszych: Użyj funkcji filter() , aby z listy liczb od 1 do 30 wybrać
#tylko liczby pierwsze. (Wskazówka: napisz pomocniczą funkcję czy_pierwsza(n) , która
#sprawdza, czy liczba jest pierwsza).



def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

liczby = list(range(1, 31))
liczby_pierwsze = list(filter(czy_pierwsza, liczby))

print(liczby_pierwsze)