# Konwersja na wielkie litery: Użyj funkcji map() , aby przekształcić listę imion imiona =
# ["anna", "piotr", "kasia"] w listę imion pisanych wielką literą.

imiona = ["anna", "piotr", "kasia"]

wielkie_imiona = list(map(str.upper, imiona))

print(wielkie_imiona)