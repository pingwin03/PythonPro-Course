# Zadanie domowe 2: Tworzenie i zarządzanie repozytorium na GitHu:

# Utwórz nowe repozytorium na GitHub (lub GitLab/Bitbucket) i sklonuj je na swój
# komputer.
# 2. Dodaj plik projekt.md i opisz w nim swój pomysł na mały projekt (np. aplikację, stronę
# internetową).
# 3. Stwórz nową gałąź feature-readme , wprowadź zmiany w pliku projekt.md i zatwierdź
# je, używając konwencji Conventional Commits (np. docs: dodano opis projektu ).
# 4. Wypchnij zmiany do zdalnego repozytorium i utwórz Pull Request na GitHubie. Upewnij
# się, że Pull Request jest czytelny i zawiera odpowiedni opis.
# 5. Zmień główną gałąź ( main lub master ) i scal Pull Request (możesz to zrobić z poziomu
# interfejsu GitHub).
# 6. Usuń lokalnie i zdalnie gałąź feature-readme , ponieważ nie jest już potrzebna.
# Oczekiwany rezultat: Repozytorium z poprawnie zarządzaną historią commitów i scalonym PR



# 1. Na GitHub: "New repository" → nadaj nazwę → "Create repository"
git clone https://github.com/TWOJ_LOGIN/NAZWA_REPO
cd NAZWA_REPO

# 2. Dodaj plik projekt.md

# Utwórz plik z opisem projektu
cat > projekt.md << 'EOF'
# Mój Projekt

## Pomysł
Aplikacja do zarządzania listą zadań (To-Do List).

## Funkcjonalności
- Dodawanie i usuwanie zadań
- Oznaczanie zadań jako ukończone
- Zapisywanie danych do pliku JSON

## Technologie
- Python 3.12
- SQLite
EOF

git add projekt.md
git commit -m "docs: inicjalizacja opisu projektu"
git push origin main


# 3. Utwórz gałąź feature-readme i wprowadź zmiany

git checkout -b feature-readme

# Edytuj projekt.md – dodaj np. sekcję Instalacja
cat >> projekt.md << 'EOF'

## Instalacja
```bash
git clone ...
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
EOF

git add projekt.md
git commit -m "docs: dodano opis projektu i instrukcję instalacji"
git push -u origin feature-readme

# 4. Utwórz Pull Request na GitHub

Wejdź na github.com → pojawi się baner "feature-readme had recent pushes" → kliknij "Compare & pull request", wypełnij:
    Tytuł:  docs: dodano opis projektu
Opis:   ## Co zostało zmienione?
        - Dodano sekcję z opisem pomysłu
        - Dodano instrukcję instalacji

        ## Dlaczego?
        Dokumentacja ułatwi onboarding nowych współpracowników.
        
        
        Kliknij "Create pull request".
        
        # 5. Scal Pull Request
        Na stronie PR kliknij "Merge pull request" → "Confirm merge". Lokalnie pobierz zmiany:
            
 git checkout main
git pull origin main

# 6. Usuń gałąź feature-readme

kliknij "Delete branch". Lokalnie:
    
    # Usuń lokalną gałąź
git branch -d feature-readme

# Usuń zdalną gałąź (jeśli nie usunięto przez GitHub)
git push origin --delete feature-readme

# Sprawdź że gałąź zniknęła
git branch -a


# efekt końcowy:
#     a1b2c3d (HEAD -> main) Merge pull request #1 from .../feature-readme
# e4f5g6h docs: dodano opis projektu i instrukcję instalacji
# i7j8k9l docs: inicjalizacja opisu projektu