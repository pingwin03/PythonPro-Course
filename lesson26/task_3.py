# Zadanie 3 – Podstawowa konfiguracja
# W projekcie z poprzedniego zadania, skonfiguruj plik settings.py zgodnie z instrukcjami z
# lekcji (dodaj odpowiednie wpisy do INSTALLED_APPS i REST_FRAMEWORK).




# core/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Dodane przeze mnie aplikacje z lekcji:
    'rest_framework',            #
    'rest_framework_simplejwt',  #
    'djoser',                    #[cite: 1]
]




# core/settings.py    

# Konfiguracja DRF, aby domyślnie używał uwierzytelniania JWT[cite: 1]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication', #[cite: 1]
    ),
}





from datetime import timedelta #[cite: 1]

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5), #[cite: 1]
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),   #[cite: 1]
}