# Parser URL: Napisz funkcję parse_url(url: str) -> dict , która przyjmuje jako
# argument adres URL w formie stringa (np.
# https://api.example.com:8080/users/search?active=true ) i zwraca słownik
# zawierający jego części: protocol , domain , port i path .
# Dla podanego przykładu, wynik powinien być: {'protocol': 'https', 'domain':
# 'api.example.com', 'port': 8080, 'path': '/users/search?active=true'} .
# Obsłuż przypadek, gdy port nie jest podany (dla http domyślny to 80, dla https 443).
# Wskazówka: Użyj metod do manipulacji stringami, takich jak split() czy find()



# Zadanie 7: Parser URL przy użyciu operacji na stringach

def parse_url(url: str) -> dict:
    # Wyciąganie protokołu
    protocol_end = url.find("://")
    if protocol_end != -1:
        protocol = url[:protocol_end]
        rest = url[protocol_end + 3:]
    else:
        protocol = "http"  # domyślny, jeśli brak
        rest = url

    # Separacja ścieżki (path) od domeny/portu
    path_start = rest.find("/")
    if path_start != -1:
        path = rest[path_start:]
        domain_and_port = rest[:path_start]
    else:
        path = "/"
        domain_and_port = rest

    # Separacja domeny i portu
    port_start = domain_and_port.find(":")
    if port_start != -1:
        domain = domain_and_port[:port_start]
        port = int(domain_and_port[port_start + 1:])
    else:
        domain = domain_and_port
        # Domyślne przypisanie portów na podstawie protokołu
        port = 443 if protocol == "https" else 80

    return {
        'protocol': protocol,
        'domain': domain,
        'port': port,
        'path': path
    }

# Test parsowania
url_example = "https://api.example.com:8080/users/search?active=true"
parsed_result = parse_url(url_example)
print("Zadanie 7 - Wynik parsowania URL:")
print(parsed_result)

# Test domyślnego portu dla https
url_no_port = "https://example.com/dashboard"
print("Dla braku portu (https):", parse_url(url_no_port))