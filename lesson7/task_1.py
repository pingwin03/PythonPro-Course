#Filtrowanie słów: Mając listę słów slowa = ["jabłko", "banan", "kiwi", "gruszka",
#"truskawka"] , użyj list comprehension, aby stworzyć nową listę zawierającą tylko te
#słowa, które mają więcej niż 5 liter

slowa = ["jabłko", "banan", "kiwi", "gruszka", "truskawka"]

dlugie_slowa = [slowo for slowo in slowa if len(slowo) > 5]

print(dlugie_slowa)