# Zadanie 9 – Zastosowanie Conventional Commits (zaawansowane)
# 1. W ramach dowolnego z poprzednich zadań, upewnij się, że wszystkie Twoje commity są
# zgodne z konwencją Conventional Commits.
# 2. Stosuj typy takie jak feat, fix, docs, style i
# dodawaj zakres, jeśli to ma sens. 
# 3. Dodatkowo, użyj opcjonalnego body (szczegółowego opisu) dla co najmniej jednego commita, wyjaśniając, dlaczego zmiana została
# wprowadzona.

cd team-project-basic

1.2.
echo "def hello_world():
    print('Hello, world!')

if __name__ == '__main__':
    hello_world()
" > app.py

git add app.py
git commit -m "feat(app): dodaj funkcję hello_world"

3.
echo "def hello_world():
    print('Hello, Rafał!')

if __name__ == '__main__':
    hello_world()
" > app.py

git add app.py
git commit -m "fix(app): zaktualizuj wiadomość w funkcji hello_world

Zmieniono wiadomość z 'Hello, world!' na 'Hello, Rafał!',
gdy projekt jest demo dla konkretnego użytkownika i lepiej
pasuje personalizowana wiadomość do kontekstu demonstracji."


SPRAWDAZAM HISTORIE: 
git log --oneline

git log
