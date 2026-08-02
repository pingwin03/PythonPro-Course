import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# [W tym miejscu znajduje się standardowa reszta pliku settings.py]

# Aktualizuję ustawienia połączenia z bazą, żeby moje Django korzystało z PostgreSQL w kontenerze.
DATABASES = {
    'default': {
        # Wskazuję, że moim silnikiem bazodanowym jest PostgreSQL.
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.getenv('DB_NAME', 'postgres'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'postgres'),
        
        # To jest kluczowy punkt! Zamiast pisać "localhost", w pole HOST wpisuję "database", 
        # czyli dokładną nazwę mojego serwisu z docker-compose.yml. 
        # Wewnętrzny serwer DNS Dockera sam przetłumaczy to na właściwy adres IP kontenera bazy.
        'HOST': os.getenv('DB_HOST', 'database'), 
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}