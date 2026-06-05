# Zadanie 10 – Praca z Git Flow (zaawansowane)
# Jeśli masz zainstalowane narzędzie git-flow (lub jesteś gotów symulować jego działanie
# ręcznymi komendami git branch/git checkout/git merge):
#  1. Zainicjalizuj git flow w nowym repozytorium.
# 2. Rozpocznij nową funkcjonalność ( git flow feature start moja-funkcja ).
# 3. Wprowadź kilka commitów na tej gałęzi.
# 4. Zakończ funkcjonalność ( git flow feature finish moja-funkcja ).
# 5. Zauważ, jak zmiany zostały scalone z gałęzią develop .
# 6. Następnie, rozpocznij gałąź wydania ( git flow release start 1.0.0 ).
# 7. Wprowadź "poprawkę" w gałęzi wydania (np. zmień coś w pliku i zatwierdź).
# 8. Zakończ wydanie ( git flow release finish 1.0.0 ). Zauważ, jak wydanie zostało
# scalone zarówno z main , jak i develop , a poprawka jest widoczna w obu gałęziach.


1.
mkdir gitflow-demo
cd gitflow-demo
git init

git flow init -d


2.
git flow feature start moja-funkcja

3.
A)
echo "# Git Flow Demo" > README.md

git add README.md
git commit -m "feat(app): dodaj plik README"

B)
echo -e "# Git Flow Demo\n\nTo jest projekt demo Git Flow." >> README.md

git add README.md
git commit -m "docs(readme): dodaj opis projektu"


SPRAWDZAM HISTORIE

git log --oneline

4.
git flow feature finish moja-funkcja

5.
To:

scala gałąź feature/moja-funkcja do develop,

usuwa gałąź feature/moja-funkcja,

przełącza z powrotem na develop.

6.
git flow release start 1.0.0

7.
echo -e "# Git Flow Demo\n\nTo jest projekt demo Git Flow.\n\n## Version: 1.0.0" >> README.md

git add README.md
git commit -m "fix(readme): dodaj numer wersji"

8.
git flow release finish 1.0.0


SPRAWDZAM:
git branch
git log --oneline --graph
git tag



