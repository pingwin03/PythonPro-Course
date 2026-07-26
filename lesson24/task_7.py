# Zadanie 7 – Przekierowanie po zalogowaniu (challenge)
# Zmodyfikuj LoginView tak, aby po zalogowaniu użytkownik był przekierowywany na stronę,
# z której przyszedł. (Wskazówka: Django robi to domyślnie, jeśli w adresie URL logowania
# jest parametr next, np. /login/?next=/profile/. Sprawdź, jak to działa w praktyce, próbując
# wejść na chronioną stronę jako niezalogowany użytkownik). Twoim zadaniem jest opisanie
# tego mechanizmu


OPISOWE ZADANIE




Automatyczne przechwytywanie: Kiedy niezalogowany użytkownik próbuje wejść na stronę chronioną dekoratorem @login_required (np. Twój profil lub stronę główną), Django automatycznie blokuje dostęp i przekierowuje go na stronę logowania.

Parametr next w adresie: Podczas tego przekierowania Django dodaje do adresu URL parametr next ze ścieżką pierwotnie żądanej strony (wygląda to mniej więcej tak: /login/?next=/profile/).

Inteligentne przekierowanie po zalogowaniu: Wbudowany LoginView w Django automatycznie odczytuje wartość tego parametru i po poprawnym wpisaniu danych logowania kieruje użytkownika bezpośrednio z powrotem na stronę, którą chciał odwiedzić, zamiast na domyślną stronę główną.

Dzięki temu mechanizmowi użytkownik nie traci kontekstu swojej nawigacji po aplikacji!