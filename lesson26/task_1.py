# Zadanie 1 – Analiza Middleware
# W nowo utworzonym projekcie Django, otwórz plik settings.py. Znajdź listę MIDDLEWARE i
# wyjaśnij w jednym zdaniu, za co (według Ciebie) odpowiadają SessionMiddleware i
# AuthenticationMiddleware.


# SessionMiddleware: Uważam, że ten komponent oprogramowania pośredniczącego 
# odpowiada bezpośrednio za zarządzanie sesjami użytkowników w naszej aplikacji.


# AuthenticationMiddleware: Z kolei ten middleware sprawdza informacje o sesji lub 
# tokenach użytkownika i dołącza obiekt request.user do każdego przychodzącego zapytania, 
# dzięki czemu mogę łatwo zweryfikować w moich widokach, czy użytkownik jest zalogowany.



