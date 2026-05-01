#Sortowanie słownika: Masz słownik oceny = {"Jan": 4, "Anna": 5, "Piotr": 3,
#"Kasia": 4} . Użyj funkcji sorted() i funkcji lambda, aby posortować elementy
#słownika (klucz, wartość) według ocen (od najwyższej do najniższej)

oceny = {"Jan": 4, "Anna": 5, "Piotr": 3, "Kasia": 4}

posortowane = sorted(oceny.items(), key=lambda x: x[1], reverse=True)

print(posortowane)