# Zadanie 7 – Rebase i interaktywna edycja historii
# Oczekiwany rezultat: Historia commitów została poprawnie zmieniona i wypchnięta.
# (challenge)
# 1. Utwórz nową gałąź feature-branch z main .
# 2. W gałęzi feature-branch wykonaj trzy oddzielne commity, każdy z małą, prostą
# zmianą (np. dodaj jedną linię do pliku, zmień drugą, dodaj komentarz).
# 3. Użyj git rebase -i HEAD~3 , aby połączyć te trzy commity w jeden spójny commit.
# Zmień typ commita na feat i użyj konwencji Conventional Commits.
# 4. Wypchnij zmiany do zdalnego repozytorium (jeśli wymagane, użyj git push --force
# – pamiętaj, że to nadpisuje historię!)

cd team-project-basic
1.
git switch main
git pull origin main

git switch -c feature-branch
git status

2.
a)
echo "# Project" > README.md

git add README.md
git commit -m "wip: add readme title"
b)
echo -e "# Project\n\nThis is a test project." >> README.md

git add README.md
git commit -m "wip: add description"
c)
echo -e "# Project\n\nThis is a test project.\n\n## Author: Rafał" >> README.md

git add README.md
git commit -m "wip: add author line"

historia:
   git log --oneline 

3.
git rebase -i HEAD~3


OTWORZY SIĘ LISTA:
pick wip: add readme title
pick wip: add description
pick wip: add author line

ZMINEIMAY DRUGI I TREZCI:
pick wip: add readme title
squash wip: add description
squash wip: add author line


OTWORZY SI Ę NOWY  PO ZAMKNIĘCIU POPRZEDNIEGO

feat: add project README with author

ZAPISZ I ZAMKNIJ

git log --oneline




4. 
git push -u origin feature-branch


LUB JEŚLI WYMAGA
git push --force origin feature-branch
