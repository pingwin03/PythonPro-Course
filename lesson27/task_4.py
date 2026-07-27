# Zadanie 4 – Zabawa z niskopoziomowym API w shellu
# Uruchom Django shell za pomocą komendy python manage.py shell. Zaimportuj from
# django.core.cache import cache. Użyj cache.set('my_key', 'hello world', 30) aby ustawić
# wartość, a następnie cache.get('my_key') aby ją odczytać. Poczekaj 30 sekund i spróbuj
# odczytać ją ponownie. Co się stało?


python manage.py shell


# Importuję obiekt cache, aby mieć do niego bezpośredni dostęp.
from django.core.cache import cache

# Ustawiam nową wartość. Zapisuję pod kluczem 'my_key' tekst 'hello world', 
# i wymuszam, aby ta informacja żyła w cache dokładnie przez 30 sekund.
cache.set('my_key', 'hello world', 30)

# Odczytuję wartość zaraz po jej ustawieniu, żeby sprawdzić, czy działa
cache.get('my_key')
# Konsola natychmiast zwraca wynik: 'hello world'

# Teraz, zgodnie z poleceniem, po prostu odczekuję 30 sekund w ciszy...

# Czas minął. Próbuję odczytać tę samą wartość ponownie
cache.get('my_key')
# Konsola nie zwraca nic (czyli zwraca obiekt None).




# Kiedy użyłem komendy cache.set, jawnie wskazałem parametr timeout=30
# . Sprawiło to, że po upływie 30 sekund klucz wygasł i został bezpowrotnie usunięty 
# z naszej lokalnej pamięci (ponieważ w settings.py używamy aktualnie locmem). 
# Dlatego też drugie odpytanie o ten sam klucz za pomocą cache.get('my_key') 
# zakończyło się brakiem danych (cache miss) i wynikiem None.