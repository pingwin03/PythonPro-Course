# Łączenie map i filter: Mając listę liczb [-5, 2, 8, -1, 0, 10] , użyj filter do
# wybrania tylko liczb dodatnich, a następnie map do obliczenia ich kwadratów. Zrób to w
# jednej linijce.


liczby = [-5, 2, 8, -1, 0, 10]
wynik = list(map(lambda x: x ** 2, filter(lambda x: x > 0, liczby)))

print(wynik)