# Zadanie 1 – Inicjalizacja repozytorium i pierwszy commit,
# 1 Zainicjalizuj nowe repozytorium Git w dowolnym katalogu na swoim komputerze.
# 2. Stwórz plik README.md i dodaj do niego krótki opis projektu.
# 3. Dodaj plik do obszaru staging i zatwierdź zmiany z odpowiednim komunikatem
# commit.
# 4. Wyświetl historię commitów za pomocą git log 
# Oczekiwany rezultat: Wykonanie poleceń git init, git add, git commit i git log poprawnie
# wyświetli historię commitów


POLECENIA

mkdir moj-projekt
cd moj-projekt

git init
git status

echo "# Mój projekt\n\nKrótki opis projektu." > README.md
git status

git add README.md
git status

git commit -m "Dodaj plik README z opisem projektu"
git status

git log