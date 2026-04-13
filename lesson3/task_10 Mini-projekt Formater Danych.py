dane = input("Podaj imię i nazwisko: ")

oczyszczone_dane = dane.strip()
sformatowane_dane = oczyszczone_dane.title()

print("Sformatowane dane:", sformatowane_dane)
print("Długość:", len(sformatowane_dane))