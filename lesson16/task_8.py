# Symulacja Klient-Serwer: Stwórz prostą symulację interakcji Klient-Serwer przy użyciu
# klas.
# Napisz klasę FakeServer , która w __init__ tworzy "bazę danych" w postaci
# słownika, np. self.db = {"users": [{"id": 1, "name": "Jan"}, {"id": 2,
# "name": "Anna"}]} .
# Klasa FakeServer powinna mieć metodę handle_request(request: dict) , która
# analizuje żądanie (reprezentowane przez słownik).
# Jeśli metoda to GET a cel to /users , powinna zwrócić słownik-odpowiedź z
# kodem 200 i listą użytkowników w ciele.
# Jeśli metoda to POST a cel to /users , powinna dodać nowego użytkownika z
# ciała żądania do self.db i zwrócić odpowiedź z kodem 201 (Created).
# Dla każdego innego żądania, zwróć odpowiedź z kodem 404 (Not Found).
# Napisz klasę FakeClient z metodą send(server, request) , która "wysyła" żądanie
# do obiektu serwera i drukuje otrzymaną odpowiedź.
# Przetestuj scenariusze: pobranie wszystkich użytkowników, dodanie nowego
# użytkownika i próbę dostępu do nieistniejącego zasobu.


# Zadanie 8: Symulacja interakcji Klient-Serwer
import json

class FakeServer:
    def __init__(self):
        # Inicjalizacja "bazy danych"
        self.db = {"users": [{"id": 1, "name": "Jan"}, {"id": 2, "name": "Anna"}]}

    def handle_request(self, request: dict) -> dict:
        method = request.get("start_line", {}).get("method")
        target = request.get("start_line", {}).get("target")
        body = request.get("body")

        if method == "GET" and target == "/users":
            return {
                "status_line": "HTTP/1.1 200 OK",
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps(self.db["users"])
            }
        
        elif method == "POST" and target == "/users":
            try:
                new_user = json.loads(body)
                # Automatyczne dodanie ID dla nowego użytkownika
                new_user["id"] = len(self.db["users"]) + 1
                self.db["users"].append(new_user)
                return {
                    "status_line": "HTTP/1.1 201 Created",
                    "headers": {"Content-Type": "application/json"},
                    "body": json.dumps(new_user)
                }
            except Exception:
                return {
                    "status_line": "HTTP/1.1 400 Bad Request",
                    "headers": {},
                    "body": "Niepoprawny format danych w ciele żądania."
                }
        
        else:
            return {
                "status_line": "HTTP/1.1 404 Not Found",
                "headers": {},
                "body": "Zasób nie istnieje."
            }

class FakeClient:
    def send(self, server: FakeServer, request: dict):
        print(f"--- Klient wysyła żądanie {request['start_line']['method']} na {request['start_line']['target']} ---")
        response = server.handle_request(request)
        print("--- Otrzymana odpowiedź z serwera ---")
        print(f"Status: {response['status_line']}")
        print(f"Headers: {response['headers']}")
        print(f"Body: {response['body']}\n")


# Scenariusz testowy
server = FakeServer()
client = FakeClient()

# 1. Pobranie wszystkich użytkowników (GET)
req_get = {
    "start_line": {"method": "GET", "target": "/users"},
    "headers": {"Host": "local.api"},
    "body": None
}
client.send(server, req_get)

# 2. Dodanie nowego użytkownika (POST)
req_post = {
    "start_line": {"method": "POST", "target": "/users"},
    "headers": {"Host": "local.api", "Content-Type": "application/json"},
    "body": '{"name": "Krzysztof"}'
}
client.send(server, req_post)

# 3. Ponowne pobranie użytkowników, by sprawdzić stan bazy (GET)
client.send(server, req_get)

# 4. Próba dostępu do nieistniejącego zasobu (404)
req_404 = {
    "start_line": {"method": "GET", "target": "/books"},
    "headers": {"Host": "local.api"},
    "body": None
}
client.send(server, req_404)