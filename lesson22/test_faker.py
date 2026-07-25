from faker import Faker

# Inicjalizacja biblioteki z polskim wariantem językowym
fake = Faker('pl_PL')

print("--- 10 LOSOWYCH POLSKICH IMION I NAZWISK ---")
for i in range(1, 11):
    # Metoda name() generuje imię i nazwisko
    print(f"{i}. {fake.name()}")

print("\n--- 10 LOSOWYCH ZDAŃ ---")
for i in range(1, 11):
    # Metoda sentence() generuje losowe zdanie
    print(f"{i}. {fake.sentence()}")