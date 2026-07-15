# PUT vs PATCH: Wyobraź sobie, że na serwerze pod adresem /users/1 znajduje się
# następujący zasób w formacie JSON: {"name": "Katarzyna", "email":
# "k.nowak@example.com", "city": "Warszawa"} .
# Opisz, jak wyglądałoby ciało żądania PUT , aby zmienić tylko imię na "Kasia".
# Opisz, jak wyglądałoby ciało żądania PATCH , aby zmienić tylko imię na "Kasia".
# Wyjaśnij w komentarzu w kodzie, dlaczego te żądania się różnią i która metoda jest
# bardziej "oszczędna" pod względem przesyłanych danych.


# Zadanie 9: PUT vs PATCH
#
# Zasób początkowy: {"name": "Katarzyna", "email": "k.nowak@example.com", "city": "Warszawa"}

# 1. Ciało żądania PUT (zastępuje cały zasób nową reprezentacją):
put_body = '{"name": "Kasia", "email": "k.nowak@example.com", "city": "Warszawa"}'

# 2. Ciało żądania PATCH (przesyła tylko modyfikowane pola/instrukcje zmian):
patch_body = '{"name": "Kasia"}'

# WYJAŚNIENIE RÓŻNIC:
# Żądania różnią się podejściem do modyfikacji zasobu. 
# Metoda PUT wymaga przesłania kompletnego obiektu wraz ze wszystkimi jego polami (nawet tymi, 
# które nie uległy zmianie). Jeśli pominiemy pole email lub city w metodzie PUT, serwer 
# najprawdopodobniej nadpisze je wartością pustą (null) lub usunie.
#
# Metoda PATCH służy do częściowej aktualizacji zasobu. Informuje serwer, aby zmodyfikował 
# wyłącznie wskazane klucze, pozostawiając resztę danych bez zmian. 
# Z tego powodu metoda PATCH jest znacznie bardziej "oszczędna" pod względem ilości 
# przesyłanych danych w sieci, ponieważ nie przesyła nadmiarowych, niezmienionych informacji.