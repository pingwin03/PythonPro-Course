# Dodaję nową konfigurację pamięci podręcznej do mojego pliku settings.py.

CACHES = {
    'default': {
        # Wskazuję Django, że chcę używać Memcached jako mojego backendu cache przy użyciu pakietu pymemcache.
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        # Podaję adres localhost i zmapowany port mojego uruchomionego kontenera Dockera.
        'LOCATION': '127.0.0.1:11211',
    }
}