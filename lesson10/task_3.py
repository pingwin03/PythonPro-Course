# Zadanie 3 – Klonowanie i współpraca.
# 1. KeyboardInterrupt.KeyboardInterrupt1. Sklonuj podane na zajęciach repozytorium z GitHub (lub stwórz własne puste
# repozytorium na GitHub i sklonuj je).
# 2. Dodaj nowy plik contributors.txt , wpisz w nim swoje imię i nazwisko.
# 3. Stwórz nową gałąź, zatwierdź zmiany i wypchnij je do zdalnego repozytorium.
# 4. Utwórz Pull Request (lub Merge Request) na platformie GitHub/GitLab/Bitbucket i
# opisz zmiany.
# Oczekiwany rezultat: Klonowanie repozytorium, dodanie pliku, utworzenie PR/MR



1. TWORZENIE NOWEGO REPOZYTORIUM:
    1.Na GitHub kliknij New repository.

2.  Podaj nazwę, zaznacz Public.

3. Nie zaznaczaj Add README ani .gitignore.

4. Kliknij Create repository.

5. Sklonuj je:
    
    git clone https://github.com/uzytkownik/nazwa-repozytorium.git
cd nazwa-repozytorium
git status



2 PLIK
echo "Rafał Duchna" > contributors.txt
git status

3. NOWA GAŁĄŹ
git switch -c feature-contributors
git status

git add contributors.txt
git commit -m "Dodaj plik contributors.txt z moim imieniem i nazwiskiem"
git status

git push -u origin feature-contributors
git status

4. 
Wejdź na GitHub w swoje repozytorium.

POJAWIA  się komunikat o niedawno wypchniętej gałęzi z przyciskiem Compare & pull request.

Kliknij Compare & pull request.

Tytuł: Dodaj plik contributors.txt.

Opis: Dodaję swój plik contributors.txt z imieniem i nazwiskiem.

Kliknij Create pull request.