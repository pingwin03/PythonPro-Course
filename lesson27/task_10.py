# Zadanie 10 – Konfiguracja Redis jako backendu cache
# To zadanie wymaga zainstalowania Redis na Twoim komputerze (np. przez Docker).
# Zainstaluj bibliotekę django-redis (pip install django-redis). Zmień konfigurację CACHES w
# settings.py, aby używać Redis jako backendu. Sprawdź za pomocą Django Debug Toolbar,
# czy Twoja aplikacja poprawnie komunikuje się z serwerem Redis. Jest to konfiguracja
# zbliżona do produkcyjnej.


Uruchomienie serwera Redis (przez Docker)

pip install django-redis


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# LOCATION: Wskazujemy na lokalny adres (127.0.0.1), udostępniony przez Dockera port (6379) 
# oraz numer domyślnej bazy danych Redisa (1).


# CLIENT_CLASS: Definiujemy domyślnego klienta, 
# który optymalizuje połączenia między Twoją aplikacją a bazą.


# Wchodzę w przeglądarce na nasz wcześniej przygotowany widok, np. [http://127.0.0.1:8000/api/products/]
# Zamiast wcześniejszych wpisów powiązanych z LocMemCache czy operacjami na plikach, w kolumnie Backend widnieje teraz  django_redis.cache.RedisCache.
# Gdy odświeżę stronę, czas wykonania operacji get drastycznie spada,
# a aplikacja w ułamku milisekundy serwuje gotowe dane pobrane prosto z pamięci RAM kontenera Redis. 
# Moja aplikacja działa teraz dokładnie w taki sam sposób, w jaki konfiguruje się prawdziwe, wydajne środowiska produkcyjne!