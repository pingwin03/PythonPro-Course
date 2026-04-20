#Silnia (rekurencja): Napisz funkcję silnia(n: int) -> int , która oblicza silnię liczby n
#w sposób rekurencyjny (czyli wywołując samą siebie). Pamiętaj o warunku bazowym: silnia
#z 0 to 1. (Wzór: n! = n * (n-1)! )

def silnia(n: int) -> int:
    if n == 0:
        return 1
    return n * silnia(n - 1)



print(silnia(0))  # 1
print(silnia(1))  # 1
print(silnia(5))  # 120
print(silnia(7))  # 5040