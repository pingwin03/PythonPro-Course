
# Zadanie 5 – Testowanie Fakera
# Napisz prosty, samodzielny skrypt .py (poza projektem Django), który importuje Faker i
# drukuje w konsoli 10 losowych polskich imion i nazwisk oraz 10 losowych zdań. (proste


tworzę plik test_faker.py

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
    
    
    
python test_faker.py



# wynik:


# (venv) PS E:\PythonPro-Course\homework\lesson22> python test_faker.py
# --- 10 LOSOWYCH POLSKICH IMION I NAZWISK ---
# 1. Liwia Dąbroś
# 2. pani Ewa Sysło
# 3. Kornel Okła
# 4. Maks Znojek
# 5. pani Angelika Waleczek
# 6. Andrzej Soroko
# 7. Ida Samiec
# 8. Mariusz Kornet
# 9. Róża Fuławka
# 10. Jędrzej Prochownik

# --- 10 LOSOWYCH ZDAŃ ---
# 1. Obywatel imię już Unia Europejska iść budować kapelusz.
# 2. Zakon dlaczego hałas powszechny przyjmować duński.
# 3. Ziemia Chrystus palec reakcja.
# 4. Białoruski wzór wzrok aż wyrób.
# 5. Istota norma studia aby już smutny.
# 6. Zapomnieć pas minuta.
# 7. Wartość pamiętać bieg koncert piwo szyja zupa.
# 8. Siedem pełnić obszar wy piec.
# 9. Rzymski lina wyrażać pozostawać wrogi wygrać ubogi.
# 10. Spadek uprawiać królowa myśleć.