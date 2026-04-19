wiek = int(input("Podaj wiek psa: "))

if wiek == 1:
    print(f"Psa ma {15} lat")
elif wiek == 2:
    print(f"Psa ma {15 + 9} lat")
else:
    print("Psa ma", 15 + 9 + (wiek - 2) * 5, "lat")