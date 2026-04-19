#Kody znaków: Używając funkcji ord() , znajdź i wyświetl kody liczbowe ASCII dla
#pierwszej litery Twojego imienia (wielką i małą literą).

pierwsza_wielka = "R"
pierwsza_mała = "r"

wielka = ord(pierwsza_wielka)
mała = ord(pierwsza_mała)

print(f"Kod pierwszej dużej litery ({pierwsza_wielka}): {wielka}")
print(f"Kod pierwszej małej litery ({pierwsza_mała}): {mała}")