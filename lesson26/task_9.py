# Zadanie 9 – Konfiguracja czasu życia tokenu
# W pliku settings.py zmień konfigurację SIMPLE_JWT tak, aby ACCESS_TOKEN_LIFETIME
# wynosił timedelta(seconds=10). Zaloguj się ponownie, aby uzyskać nowy token. Spróbuj
# użyć go do odpytania chronionego endpointu z zadania 8. Odczekaj 10 sekund i spróbuj
# ponownie. Jaką odpowiedź otrzymałeś za drugim razem?



# core/settings.py

from datetime import timedelta

# ... reszta pliku ...

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(seconds=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    # pozostałe ustawienia, np. AUTH_HEADER_TYPES itp.
}



test odpowiedź
{
    "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": [
        {
            "token_class": "AccessToken",
            "token_type": "access",
            "message": "Token is invalid or expired"
        }
    ]
}