# Dekorator logujący: Napisz dekorator @loguj , który przed wywołaniem udekorowanej
# funkcji wypisze komunikat Uruchamiam funkcję [nazwa_funkcji]... , a po jej
# zakończeniu Zakończono funkcję [nazwa_funkcji].




# def loguj(func: callable):
#     def wrapper(*args, **kwargs):
#         print(f"uruchamiam funkcję {func.__name__}")
#         res = func(*args, **kwargs)
#         print(f"zakończono funckję {func.__name__}")
#         return res
#     return wrapper
# @loguj
# def dodaj(a, b):
#     return a + b
# print(dodaj(2, 3))

from functools import wraps

def loguj(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Uruchamiam funkcję {func.__name__}...")
        wynik = func(*args, **kwargs)
        print(f"Zakończono funkcję {func.__name__}.")
        return wynik
    return wrapper


@loguj
def witaj(imie):
    print(f"Cześć, {imie}!")


witaj("Rafał")