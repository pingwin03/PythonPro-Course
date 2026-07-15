# Zadanie 3: Model żądania GET w formie słownika
# Model żądania: Utwórz w Pythonie słownik, który będzie reprezentował żądanie GET w
# celu pobrania listy wszystkich artykułów z adresu /api/articles . W nagłówkach dodaj
# klucz Host z wartością my-blog.com 


http_get_request = {
    "start_line": {
        "method": "GET",
        "target": "/api/articles",
        "version": "HTTP/1.1"
    },
    "headers": {
        "Host": "my-blog.com",
        "User-Agent": "VisualStudioClient/1.0",
        "Accept": "application/json"
    },
    "body": None
}

print("Zadanie 3 - Żądanie GET:")
print(http_get_request)