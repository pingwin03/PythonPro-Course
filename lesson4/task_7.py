# Program, który świadomie próbuje przekonwertować słowo "Python" na liczbę całkowitą:

# BŁĘDNA LINIA (powoduje ValueError):
# liczba = int("Python")

# Wyjaśnienie, dlaczego kod nie działał (gdyby linia była aktywna):
# - funkcja int() konwertuje tylko tekst reprezentujący liczbę (np. "42", "-7", "0").
# - słowo "Python" nie jest liczbą, więc Python nie może go przekonwertować.
# - wynik: interpreter zgłasza błąd ValueError: invalid literal for int() with base 10: 'Python'

# Wersja NAPRAWIONA: błędna linia jest w komentarzu, program nie kończy się wyjątkiem.
print("Program świadomie próbuje konwersji słowa 'Python' na liczbę całkowitą.")
print("Gdyby linia 'liczba = int(\"Python\")' była aktywna, pojawił się błąd:")
print("ValueError: invalid literal for int() with base 10: 'Python'")
print("Dzieje się tak, ponieważ int() konwertuje tylko tekst, który jest liczbą.")
print("Słowo 'Python' nie reprezentuje liczby, więc konwersja kończy się błędem.")
