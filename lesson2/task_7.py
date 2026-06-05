#Praktyka z venv :
#Utwórz folder project_test .
#Wewnątrz niego utwórz środowisko wirtualne venv .
#Aktywuj je.
#Wykonaj polecenie pip list , aby zobaczyć, że nie ma zainstalowanych bibliotek.
#Dezaktywuj środowisko


# 1. Utwórz folder project_test
mkdir project_test

# 2. Wejdź do niego
cd project_test

# 3. Utwórz środowisko wirtualne o nazwie venv
py -m venv venv
# albo: python -m venv venv

# 4. Aktywuj środowisko
venv\Scripts\activate
# w PowerShell: venv\Scripts\Activate.ps1

# 5. Sprawdź listę zainstalowanych pakietów
pip list
powinieneś zobaczyć tylko pip i setuptools (lub podobne) – bez dodatkowych bibliotek.

# 6. Dezaktywuj środowisko
deactivate