# Zadanie 1 – Konfiguracja settings.py (proste)
# W pliku settings.py swojego projektu dodaj zmienne LOGIN_REDIRECT_URL oraz
# LOGOUT_REDIRECT_URL. Pierwsza powinna wskazywać na stronę główną ('/' lub nazwę
# URL strony głównej), a druga na stronę logowania.


# projekt_auth/settings.py

# ... ( na samym końcu pliku dopisuję:)

LOGIN_REDIRECT_URL = '/'  # Przekierowanie na stronę główną po zalogowaniu
LOGOUT_REDIRECT_URL = 'login'  # Przekierowanie na stronę logowania po wylogowaniu