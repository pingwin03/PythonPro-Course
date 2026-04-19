 #Tworzenie dwóch różnych list z identyczną zawartością
lista1 = [1, 1]
lista2 = [1, 1]

# Porównanie za pomocą '==' (równość wartości)
print(f"lista1 == lista2: {lista1 == lista2}")

# Porównanie za pomocą 'is' (tożsamość obiektów)
print(f"lista1 is lista2: {lista1 is lista2}")


#== (porównanie wartości) sprawdza, czy zawartość list jest taka sama - czy zawierają identyczne elementy w tej samej kolejności. 
# Ponieważ obie listy mają [1, 1], wynik to True.

#is (porównanie tożsamości) sprawdza, czy obie zmienne wskazują na ten sam obiekt w pamięci. 
# Python utworzył dwie oddzielne listy w różnych miejscach pamięci, mimo identycznej zawartości, dlatego lista1 is lista2 zwraca False