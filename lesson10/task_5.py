# Zadanie 5 – Praca z plikami i commitami
# 1. W repozytorium team-project-basic (z Zadania 4) stwórz plik app.py z prostym
# kodem Pythona (np. funkcja hello_world ).
# 2. Dodaj app.py do obszaru staging.
# 3. Wykonaj commit z komunikatem zgodnym z Conventional Commits (np. feat: add
# hello world function ).
# 4. Zmodyfikuj app.py (np. zmień komunikat funkcji).
# 5. Sprawdź status repozytorium ( git status ).
# 6. Dodaj zmieniony plik do stagingu i wykonaj kolejny commit (np. fix: update hello world
# message).


cd team-project-basic
1.
echo "def hello_world():
    print('Hello, world!')

if __name__ == '__main__':
    hello_world()
" > app.py

cat app.py

2. 
git add app.py
git status

3.
git commit -m "feat: add hello world function"
git log --oneline

4.
echo "def hello_world():
    print('Hello, Rafał!')

if __name__ == '__main__':
    hello_world()
" > app.py

cat app.py
5.
git status

6. 
git add app.py
git commit -m "fix: update hello world message"
git log --oneline
git status