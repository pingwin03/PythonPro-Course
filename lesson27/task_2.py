# Zadanie 2 – Instalacja Django Debug Toolbar
# Zainstaluj i skonfiguruj django-debug-toolbar zgodnie z instrukcjami z lekcji. Upewnij się, że
# panel jest widoczny w Twojej aplikacji i możesz wejść w zakładkę "Cache".





pip install django-debug-toolbar





# cache_project/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'store',
    'debug_toolbar', # Dodaję Debug Toolbar
]





# cache_project/settings.py

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware', # Dodaję middleware dla Debug Toolbara
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



# cache_project/settings.py

INTERNAL_IPS = [
    '127.0.0.1', # Konfiguruję adres dla środowiska lokalnego
]




# cache_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Dodaję ścieżki dla Debug Toolbara[cite: 1]
    path('__debug__/', include('debug_toolbar.urls')), 
]



python manage.py createsuperuser

python manage.py runserver




http://127.0.0.1:8000/admin/