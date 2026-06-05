# Zadanie domowe 3: Rozwiązywanie konfliktów w Git
# 1.	Utwórz repozytorium lokalnie i zainicjalizuj Git ( git init ).
# 2.  Dodaj plik konflikt.txt , wpisz do niego pierwszą linię tekstu (np. "Pierwsza linia
# tekstu.") i wykonaj commit ( git commit -m "feat: dodano poczatkowy tekst" ).
# 3. Utwórz nową gałąź galaz-A ( git checkout -b galaz-A ) i edytuj konflikt.txt ,
# dodając nową linię w środku pliku (np. "Linia dodana w galaz-A."). Zatwierdź zmiany ( git
# commit -m "feat: dodano linie z galaz-A" ).
# 4. Przełącz się na main ( git checkout main ) i również edytuj konflikt.txt , dodając
# inną nową linię w tym samym miejscu w pliku (np. "Linia dodana w main."). Zatwierdź
# zmiany ( git commit -m "feat: dodano linie z main" ).
# 5. Spróbuj scalić galaz-A z main ( git merge galaz-A ). Zauważysz konflikt.
# 6. Rozwiąż powstały konflikt w pliku konflikt.txt , edytując go ręcznie tak, aby zawierał
# obie dodane linie (np. "Pierwsza linia tekstu.\nLinia dodana w galaz-A.\nLinia dodana w
# main."). Następnie dodaj rozwiązany plik do stagingu ( git add konflikt.txt ).
# 7. Zatwierdź poprawioną wersję pliku i zakończ scalanie ( git commit -m "merge:
# rozwiazano konflikt w konflikt.txt" )

# Oczekiwany rezultat: Poprawnie rozwiązany konflikt merge w pliku konflikt.txt


# 1–2. Inicjalizacja repozytorium i pierwszy commit
mkdir repo_konflikt
cd repo_konflikt
git init

echo "Pierwsza linia tekstu." > konflikt.txt
git add konflikt.txt
git commit -m "feat: dodano poczatkowy tekst"

# 3. Gałąź galaz-A – edycja pliku
git checkout -b galaz-A

# Dodaj drugą linię
echo "Linia dodana w galaz-A." >> konflikt.txt

git add konflikt.txt
git commit -m "feat: dodano linie z galaz-A"

# 4. Powrót na main – edycja tego samego miejsca
git checkout main

# Dodaj inną linię w tym samym miejscu
echo "Linia dodana w main." >> konflikt.txt

git add konflikt.txt
git commit -m "feat: dodano linie z main"

# 5. Próba scalenia – konflikt!
git merge galaz-A

Git wyświetli:
    
Auto-merging konflikt.txt
CONFLICT (content): Merge conflict in konflikt.txt
Automatic merge failed; fix conflicts and then commit the result.

# Plik konflikt.txt będzie wyglądał tak:
Pierwsza linia tekstu.
<<<<<<< HEAD
Linia dodana w main.
=======
Linia dodana w galaz-A.
>>>>>>> galaz-A
# Znaczniki konfliktu oznaczają: <<<<<<< HEAD to wersja z bieżącej gałęzi (main), ======= to separator, >>>>>>> galaz-A to wersja z gałęzi scalającej.

# 6. Rozwiązanie konfliktu – edycja ręczna
# Otwórz konflikt.txt w edytorze i zastąp cały blok ze znacznikami finalną wersją:
Pierwsza linia tekstu.
Linia dodana w galaz-A.
Linia dodana w main.
# Usuń wszystkie znaczniki (<<<<<<<, =======, >>>>>>>). Następnie:
git add konflikt.txt

# 7. Zatwierdzenie scalenia
git commit -m "merge: rozwiazano konflikt w konflikt.txt"

# Weryfikacja – historia commitów
git log --oneline --graph
# Powinno wyglądać tak:
*   a1b2c3d (HEAD -> main) merge: rozwiazano konflikt w konflikt.txt
|\
| * e4f5g6h (galaz-A) feat: dodano linie z galaz-A
* | i7j8k9l feat: dodano linie z main
|/
* m1n2o3p feat: dodano poczatkowy tekst
# Flaga --graph rysuje rozgałęzienie i scalenie w ASCII — widać dokładnie gdzie gałęzie się rozeszły i połączyły.