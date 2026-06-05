# Zadanie 8 – Rozwiązywanie konfliktów w Git
# 1. Utwórz repozytorium lokalnie i zainicjalizuj Git ( git init ).
# 2. Dodaj plik conflict_example.txt , wpisz do niego pierwszą linię tekstu (np. Linia
# 1 - wersja glowna ) i wykonaj commit ( git commit -m "feat: dodano pierwsza
# linie" ).
# 3. Utwórz nową gałąź branch-A ( git checkout -b branch-A ) i edytuj
# conflict_example.txt , dodając drugą linię (np. Linia 2 - z branch-A ).
# Zatwierdź zmiany ( git commit -m "feat: dodano druga linie w branch-A" ).
# 4. Przełącz się na main ( git checkout main ) i również edytuj
# conflict_example.txt , ale w inny sposób (np. zmień pierwszą linię na Linia 1 -
# zmieniona w main i dodaj nową linię Linia 2 - z main ). Zatwierdź zmiany ( git
# commit -m "fix: zmieniono pierwsza linie i dodano druga w main" ).
# 5. Spróbuj scalić branch-A z main ( git merge branch-A ). Zauważysz konflikt.
# 6. Rozwiąż powstały konflikt w pliku conflict_example.txt , edytując go ręcznie, a
# następnie dodaj rozwiązany plik do stagingu ( git add conflict_example.txt ).
# 7. Zatwierdź poprawioną wersję pliku i zakończ scalanie ( git commit )

# Oczekiwany rezultat: Poprawnie rozwiązany konflikt merge w pliku conflict_example.txt.
# (challenge)

1.
mkdir conflict-repo
cd conflict-repo
git init

2.
echo "Linia 1 - wersja glowna" > conflict_example.txt

git add conflict_example.txt
git commit -m "feat: dodano pierwsza linie"

3.
git checkout -b branch-A

echo -e "Linia 1 - wersja glowna\nLinia 2 - z branch-A" > conflict_example.txt

git add conflict_example.txt
git commit -m "feat: dodano druga linie w branch-A"

4.
git checkout main

echo -e "Linia 1 - zmieniona w main\nLinia 2 - z main" > conflict_example.txt

git add conflict_example.txt
git commit -m "fix: zmieniono pierwsza linie i dodano druga w main"

5.
git merge branch-A
GIT ZGOSI KONFLIKT W PLIKU

6.
<<<<<< HEAD
Linia 1 - zmieniona w main
Linia 2 - z main
======
Linia 1 - wersja glowna
Linia 2 - z branch-A
>>>>>> branch-A

POPRAWIAMY

Linia 1 - zmieniona w main
Linia 2 - z main
Linia 2 - z branch-A
ZAPISUJEMY


7.
git add conflict_example.txt

git commit -m "merge: rozwiazano konflikt merge branch-A z main"

HISTORIA:
    git log --oneline --graph