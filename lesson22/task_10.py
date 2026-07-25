# Zadanie 10 – Rejestracja i Logowanie
# Zintegruj z projektem zewnętrzną aplikację do obsługi użytkowników, np. django-allauth.
# Skonfiguruj ją tak, aby użytkownicy mogli się rejestrować i logować. To duże zadanie, które
# wymaga czytania dokumentacji, ale jest to kluczowa umiejętność w pracy z frameworkami.
# (challenge)

# w terminalu:
    
    
pip install django-allauth

# Konfiguracja w settings.py


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Dodaję framework "sites", który jest wymagany przez allauth
    'django.contrib.sites',

    # Dodaję główne aplikacje allauth do mojego projektu
    'allauth',
    'allauth.account',
    
    # Moja aplikacja bloga
    'blog',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # Dodaję middleware z allauth, aby obsługiwał specyficzne żądania związane z kontami
    'allauth.account.middleware.AccountMiddleware',
]




# Ustawiam ID mojej strony, co jest absolutnie wymagane przez aplikację "sites" i allauth
SITE_ID = 1

# Konfiguruję backendy autentykacji, aby móc logować się standardowo w Django oraz przez allauth
AUTHENTICATION_BACKENDS = [
    # Standardowe logowanie w panelu admina Django
    'django.contrib.auth.backends.ModelBackend',
    # Specyficzne metody uwierzytelniania allauth (np. logowanie adresem e-mail)
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Definiuję, gdzie aplikacja ma mnie przekierować po udanym zalogowaniu
# Zmienimy to później na nazwę widoku strony głównej, na razie przekierowuję na główny adres
LOGIN_REDIRECT_URL = '/'

# Konfiguruję, aby allauth nie wymagał weryfikacji e-mail przy rejestracji (dla uproszczenia w fazie developmentu)
ACCOUNT_EMAIL_VERIFICATION = 'none'



# Podłączenie ścieżek URL (urls.py)


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Podłączam wszystkie widoki związane z autentykacją z biblioteki allauth 
    # pod ścieżkę /accounts/ (np. /accounts/login/, /accounts/signup/)
    path('accounts/', include('allauth.urls')),
    
    # Tutaj pewnie masz już podłączone ścieżki swojego bloga
    # path('', include('blog.urls')),
]




python manage.py migrate





Rejestracja: [http://127.0.0.1:8000/accounts/signup/]
Logowanie: [http://127.0.0.1:8000/accounts/login/]
Wylogowanie: [http://127.0.0.1:8000/accounts/logout/]