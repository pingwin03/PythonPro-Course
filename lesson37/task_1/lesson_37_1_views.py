from django.http import HttpResponse
from django.core.cache import cache

def verify_memcached_connection(request):
    # Próbuję zapisać testową wartość w moim kontenerze Memcached. Ustawiam czas życia (TTL) na 60 sekund.
    cache.set('moj_testowy_klucz', 'Połączenie z kontenerem Memcached zakończone sukcesem!', timeout=60)
    
    # Od razu próbuję pobrać zapisaną wartość, aby upewnić się, że komunikacja działa w obie strony.
    wynik_z_cache = cache.get('moj_testowy_klucz')
    
    if wynik_z_cache:
        # Jeśli dane wrócą z cache, wyświetlam komunikat o sukcesie.
        return HttpResponse(f"Sukces: {wynik_z_cache}")
    
    # Jeśli wartość wynosi None, informuję o problemie z połączeniem.
    return HttpResponse("Błąd: Nie udało mi się odczytać wartości z Memcached. Sprawdź, czy kontener na pewno działa na porcie 11211.")