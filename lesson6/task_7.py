#Zwracanie wielu wartości: Stwórz funkcję analiza_listy(lista: list[int]) , która
#przyjmuje listę liczb i zwraca krotkę zawierającą trzy wartości: minimum, maksimum i sumę
#elementów z listy


def analiza_listy(lista: list[int]) -> tuple[int, int, int]:
    return min(lista), max(lista), sum(lista)


liczby = [4, 1,7, 2, 8, 9]

minimum, maksimum, suma = analiza_listy(liczby)
print(f"Minimum: {minimum}, Maksimum: {maksimum}, Suma: {suma}")

