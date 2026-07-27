# Zadanie 6 – Implementacja cache plikowego
# Zmień konfigurację cache w settings.py na FileBasedCache. Stwórz odpowiedni katalog.
# Użyj widoku z zadania 3. Sprawdź, czy po pierwszym odwołaniu do widoku w Twoim
# katalogu cache pojawiły się nowe pliki. Co zawierają te pliki?


# cache_project/settings.py

# Upewniam się, że na górze pliku zaimportowany jest moduł os (jeśli nie ma go domyślnie)
import os

# Podmieniam poprzednią konfigurację locmem z Zadania 1 na FileBasedCache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        # Określam ścieżkę do katalogu, który znajdzie się w głównym folderze mojego projektu
        'LOCATION': os.path.join(BASE_DIR, 'django_cache'), 
    }
}


# Utworzenie odpowiedniego katalogu

mkdir django_cache

po uruchomieniu serwera WCHODZĘ:
    http://127.0.0.1:8000/products/
    
Co pojawiło się w katalogu cache i co zawierają te pliki?
Kiedy zaglądam do świeżo utworzonego folderu E:\PythonPro-Course\homework\lesson27\django_cache, 
widzę w nim nowe pliki z bardzo długimi, losowymi nazwami składającymi się ze znaków alfanumerycznych

1f3f3cc35535b57cd62fe43f574ff0a9.djcache


PLIKI W ŚRODKU ZAWIERAJĄ
1. Znacznik czasu wygaśnięcia (timeout): Informację o tym, kiedy dany klucz traci ważność, 
aby system wiedział, kiedy przestać z niego korzystać.

2. Pełną treść odpowiedzi: Zserializowany obiekt zapytania z naszego widoku, 
w tym nasze wygenerowane dane z bazy (produkty, które dodaliśmy z poziomu shella) 
oraz odpowiednie nagłówki HTTP potrzebne do odtworzenia pełnej odpowiedzi HTTP przy 
kolejnym żądaniu ("cache hit").