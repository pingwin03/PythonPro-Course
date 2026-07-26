# Zadanie 1 – Instalacja i konfiguracja
# (proste)
# Stwórz nowy projekt Django. Zainstaluj Django REST Framework (pip install
# djangorestframework) i dodaj 'rest_framework' do INSTALLED_APPS w ustawieniach
# projektu.


python -m venv venv
venv\Scripts\activate

# Instaluję framework Django oraz wskazaną w zadaniu bibliotekę DRF
pip install django djangorestframework

# Tworzę mój nowy projekt Django, który nazwę np. 'my_api_project'
django-admin startproject my_api_project

# Wchodzę do folderu mojego nowego projektu
cd my_api_project



# my_api_project/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Zgodnie z poleceniem zadania, dodaję DRF do moich zainstalowanych aplikacji
    'rest_framework',
]