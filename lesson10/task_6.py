#  Zadanie 6 – Resetowanie i przywracanie zmian
# 1. Wprowadź kilka zmian w istniejącym pliku i dodaj je do stagingu ( git add ).
# 2. Wycofaj te zmiany z obszaru staging ( git reset HEAD <plik> ).
# 3. Wprowadź kolejne zmiany w tym samym pliku i wykonaj commit.
# 4. Cofnij się do commita sprzed tych ostatnich zmian za pomocą git reset --hard
# <hash_commita> . Upewnij się, że rozumiesz, co robi --hard
# Oczekiwany rezultat: Zmiany poprawnie cofnięte lub przywrócone do wcześniejszego stanu.

cd team-project-basic



1.
echo "def hello_world():
    print('Hello, Rafał!')

def add(a, b):
    return a + b

if __name__ == '__main__':
    hello_world()
    print(add(2, 3))
" > app.py

git add app.py
git status





2.
git reset HEAD app.py
git status

3.
echo "def hello_world():
    print('Hello, Rafał!')

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

if __name__ == '__main__':
    hello_world()
    print(add(2, 3))
    print(multiply(2, 3))
" > app.py

git add app.py
git commit -m "feat: add multiply function"
git log --oneline


4.
git log --oneline

git reset --hard a1b2c3d
git log --oneline
git status