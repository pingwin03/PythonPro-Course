# Klasa Request : Napisz klasę w Pythonie o nazwie HttpRequest .
# Konstruktor __init__ powinien przyjmować method , target oraz opcjonalnie
# headers (słownik) i body (string).
# Dodaj metodę display() , która będzie drukować sformatowane żądanie na konsoli w
# czytelnej formie, np.:
# --- HTTP Request ---
# Method: GET
# Target: /index.html
# Headers:
# Host: example.com
# User-Agent: PythonClient/1.0
# Body:
# (empty)
# --------------------


# Zadanie 6: Klasa HttpRequest

class HttpRequest:
    def __init__(self, method, target, headers=None, body=None):
        self.method = method
        self.target = target
        self.headers = headers if headers is not None else {}
        self.body = body

    def display(self):
        print("HTTP Request")
        print(f"Method: {self.method}")
        print(f"Target: {self.target}")
        print("Headers:")
        if self.headers:
            for key, value in self.headers.items():
                print(f"  {key}: {value}")
        else:
            print("  (no headers)")
        print("Body:")
        if self.body:
            print(f"  {self.body}")
        else:
            print("  (empty)")
        print("-" * 30)

# Testowanie klasy dla żądania POST
post_headers = {
    "Host": "example.com",
    "Content-Type": "application/json"
}
post_body = '{"title": "Nowy Post", "content": "Treść zadania"}'

post_request = HttpRequest(method="POST", target="/api/posts", headers=post_headers, body=post_body)
print("Zadanie 6 - Prezentacja klasy HttpRequest:")
post_request.display()