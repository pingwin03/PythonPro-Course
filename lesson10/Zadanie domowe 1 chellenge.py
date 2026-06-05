# Zadanie domowe 1: Zespołowe tworzenie małego projektu
# Przygotowanie projektu (1 godzina)
# 1.	Tworzenie repozytorium:
# Utwórz nową repozytorię na GitHub/GitLab.
# Skonfiguruj ochronę gałęzi dla gałęzi main (np. wymagaj 2 recenzentów, wymagaj
# przejścia testów, zablokuj bezpośrednie commity).
# Dodaj pliki .gitignore (dla Pythona) i README.md (z opisem projektu).
# Skonfiguruj Git Flow (jeśli używasz narzędzia git-flow lub stwórz gałąź
# develop ręcznie)
# 2.	Konfiguracja środowiska:
# # Klonowanie repozytorium
# git clone https://pl.wikipedia.org/wiki/Repozytorium # Zastąp to rzeczywistym URL repozytorium
# cd [nazwa projektu]
# # Inicjalizacja Git Flow (jeśli nie zrobiono wcześniej)
# # git flow init
# # Tworzenie podstawowej struktury
# mkdir src tests docs



1. Utwórz repozytorium na GitHub
Wejdź na github.com → "New repository" → wypełnij nazwę, zaznacz "Add README.md" i "Add .gitignore" (wybierz szablon Python).

2. Sklonuj i skonfiguruj strukturę
git clone https://github.com/TWOJ_LOGIN/NAZWA_REPO
cd NAZWA_REPO

# Tworzenie struktury katalogów
mkdir src tests docs

# Tworzenie gałęzi develop (Git Flow)
git checkout -b develop
git push -u origin develop

3. Ochrona gałęzi main (na GitHub)
Wejdź w: Settings → Branches → Add rule → wpisz main, zaznacz:

✅ Require a pull request before merging
✅ Require approvals (ustaw: 2)
✅ Require status checks to pass
✅ Block direct pushes (Do not allow bypasses)

4. Konfiguracja środowiska wirtualnego

python -m venv venv
source  venv\Scripts\activate        
     # Windows

pip install pytest
pip freeze > requirements.txt

touch src/__init__.py tests/__init__.py
Zaktualizuj README.md:
    
# Nazwa Projektu

## Opis
Krótki opis projektu.

## Instalacja
```bash
git clone ...
cd nazwa_projektu
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Uruchomienie testów
```bash
pytest tests/
```

6. Pierwszy commit na develop
git add .
git commit -m "chore: inicjalizacja struktury projektu"
git push origin develop


git checkout develop
git checkout -b feature/moja-funkcja
# ... praca ...
git push origin feature/moja-funkcja
# → otwierasz Pull Request do develop na GitHub