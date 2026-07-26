# Zadanie 10 – Odświeżanie tokenu
# Wykorzystaj refresh token, który otrzymałeś podczas logowania. Wyślij zapytanie POST na
# endpoint /auth/jwt/refresh/ z ciałem { "refresh": "<twój_refresh_token>" }. W odpowiedzi
# powinieneś otrzymać nowy, świeży access token. Sprawdź, czy ten nowy token działa,
# odpytując chroniony endpoint.



w postmanie

Ustawiam metodę na POST

http://127.0.0.1:8000/auth/jwt/refresh/


{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5c..." 
}


# Wygenerowanie nowego access tokenu
# Klikam Send. W odpowiedzi od serwera (status 200 OK) otrzymuję krótki obiekt JSON,
# w którym znajduje się wyłącznie jeden klucz: nowiutki access. Mój stary refresh token
# został pomyślnie zweryfikowany i na jego podstawie wygenerowano mi nowy bilet wstępu na kolejne 10 sekund.



Kopiuję ten nowo otrzymany ciąg access
Wracam do zakładki z moim zapytaniem GET na chroniony endpoint
http://127.0.0.1:8000/api/protected/
W zakładce Headers podmieniam stary, wygasły token na ten nowy (zostawiając Bearer  na początku).
send
Otrzymuję status 200 OK oraz informację: {"username": "nowy_uzytkownik"}. Endpoint prawidłowo przepuścił zapytanie.