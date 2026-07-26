# Zadanie 6 – Logowanie i inspekcja tokenu
# Używając Postmana, wyślij zapytanie POST na endpoint /auth/jwt/create/, aby zalogować
# użytkownika utworzonego w poprzednim zadaniu. Skopiuj otrzymany access token i wklej
# go na stronie jwt.io. Przeanalizuj zdekodowane dane w sekcji "Payload". Czy widzisz tam
# user_id? Jaki jest czas wygaśnięcia (exp)?


postman
Jako adres URL podaję endpoint do logowania: [http://127.0.0.1:8000/auth/jwt/create/]
{
    "username": "nowy_uzytkownik",
    "password": "bardzoTrudneHaslo123"
}

Inspekcja tokenu na jwt.io


Widzę klucz user_id. Wartość przypisana do tego klucza to numer ID mojego użytkownika w bazie danych Django 
(ppodobnie 2, ). Biblioteka simplejwt 
domyślnie umieszcza tam ten identyfikator, aby serwer po rozkodowaniu tokenu wiedział, kto dokładnie wysyła zapytanie.



Widzę tam klucz exp z dużą wartością liczbową "exp": 1785067883,. Jest to Unix Timestamp (czas uniksowy)
– liczba sekund, jaka upłynęła od 1 stycznia 1970 roku. 
Ponieważ w Zadaniu 3 skonfigurowaliśmy ACCESS_TOKEN_LIFETIME na 5 minut, 
wartość exp wskazuje dokładnie czas 5 minut w przód od momentu kliknięcia "Send" w Postmanie. 
(Strona jwt.io jest na tyle sprytna, że po najechaniu kursorem na tę liczbę wyświetla czytelną datę i godzinę, 
 więc mogę to łatwo zweryfikować!).