punkt = (10, 20, 30)

# Próba zmiany elementu krotki spowoduje błąd,
# ponieważ krotki są niemutowalne — nie można ich modyfikować po utworzeniu.
# punkt[0] = 15


try:
    punkt[0] = 15
except TypeError:
    print("Błąd: krotka jest niemutowalna, więc nie można zmienić jej elementu.")
