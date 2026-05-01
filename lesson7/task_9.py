# Dekorator z argumentem: Stwórz dekorator @powtorz(n) , który przyjmuje argument n i
# powoduje, że udekorowana funkcja zostanie wykonana n razy.


from functools import wraps

def powtorz(n):
    def dekorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return dekorator


@powtorz(3)
def witaj():
    print("Cześć!")


witaj()