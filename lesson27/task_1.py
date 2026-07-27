# Zadanie 1 – Konfiguracja locmem cache
# W swoim projekcie Django, w pliku settings.py, skonfiguruj domyślny cache tak, aby używał
# django.core.cache.backends.locmem.LocMemCache. Uruchom serwer, aby upewnić się, że
# aplikacja startuje bez błędów.




# settings.py

CACHES = {
    'default': {
        # Wskazuję backend lokalnej pamięci podręcznej dla procesu.
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        # Nadaję unikalną nazwę dla mojej instancji cache.
        'LOCATION': 'unique-snowflake', 
    }
}



# serewer działa:
#     Watching for file changes with StatReloader
# Performing system checks...

# System check identified no issues (0 silenced).
# July 26, 2026 - 18:33:13
# Django version 6.0.7, using settings 'cache_project.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CTRL-BREAK.

# WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
# For more information on production servers see: https://docs.djangoproject.com/en/6.0/howto/deployment/