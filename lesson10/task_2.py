# Zadanie 2 – Praca z gałęziami
# 1. Utwórz nową gałąź o nazwie feature-login .
# 2. Przełącz się na nową gałąź i dodaj nowy plik login.py (lub login.html jeśli wolisz).
# 3. Zatwierdź zmiany w tej gałęzi i przełącz się z powrotem na main .
# 4. Spróbuj połączyć gałąź feature-login z main i rozwiąż ewentualne konflikty.
# Oczekiwany rezultat: Powstanie nowej gałęzi, zatwierdzenie zmian, scalanie bez błędów lub
# rozwiązanie konfliktów



POLECENIA:

git branch feature-login
git switch feature-login
git status

echo "print('Login module')" > login.py
git status

git add login.py
git commit -m "Dodaj plik login.py"
git status

git switch main
git status

git merge feature-login
git status

GDY BĘDZIE KONFLIKT:
git add .
git commit -m "Rozwiąż konflikt scalania feature-login"