def oblicz_srednia(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)


print(oblicz_srednia(4, 3, 5))     #dowolna liczba OCEN ZWRACA  ŚREDNIĄ


print(oblicz_srednia())    #bez oceny zwraca 0