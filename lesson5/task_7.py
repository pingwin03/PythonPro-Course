zdanie = input("Podaj zdanie: ")

for litera in zdanie:
    if litera.lower() not in "aeiouy":
        continue
    print(litera)