# Zadanie 4 – GraphQL - Query użytkownika
# Stwórz prosty GraphQL API z typem User(id, name, email) i query user(id: ID!)
# zwracającym użytkownika z fake listy


import strawberry
from typing import Optional
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView

# Definiuję mój typ GraphQL dla użytkownika
@strawberry.type
class User:
    # Używam wbudowanego typu ID ze strawberry dla identyfikatora
    id: strawberry.ID
    name: str
    email: str

# Tworzę moją "fałszywą" bazę danych (listę obiektów User)
fake_users_db = [
    User(id=strawberry.ID("1"), name="Jan Kowalski", email="jan@example.com"),
    User(id=strawberry.ID("2"), name="Anna Nowak", email="anna@example.com"),
    User(id=strawberry.ID("3"), name="Piotr Wiśniewski", email="piotr@example.com"),
]

# Definiuję główne zapytania (Queries) dla mojego API
@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: strawberry.ID) -> Optional[User]:
        """Szukam i pobieram użytkownika na podstawie jego ID"""
        # Przeszukuję moją listę w poszukiwaniu dopasowania
        for user in fake_users_db:
            if user.id == id:
                return user
        # Jeśli nie znajdę użytkownika, zwracam None
        return None

# Tworzę mój schemat GraphQL, przekazując klasę Query
schema = strawberry.Schema(query=Query)

# Przygotowuję i uruchamiam moją aplikację webową
app = web.Application()

# Dodaję endpoint GraphQL z włączonym interfejsem GraphiQL do testów
app.router.add_route("*", "/graphql", GraphQLView(schema=schema))

if __name__ == '__main__':
    print("Moje API GraphQL działa na http://localhost:8000/graphql")
    print("Mogę otworzyć ten link w przeglądarce, aby przetestować zapytania w GraphiQL")
    web.run_app(app, host='localhost', port=8000)
    
    
    
# test:
 
#  Uruchamiam powyższy skrypt (python task_4.py).
#  Otwieram w przeglądarce adres http://localhost:8000/graphql.  
#  W interfejsie GraphiQL wpisuję po lewej stronie następujące zapytanie:
#      GraphQLquery {
#   user(id: "2") {
#     name
#     email
#   }
# }
# Po kliknięciu przycisku "Play" , po prawej stronie otrzymałem precyzyjną odpowiedź w 
# formacie JSON z danymi Anny Nowak, ponieważ dokładnie o te pola poprosiłem w moim zapytaniu.   


# {
#   "data": {
#     "user": {
#       "name": "Anna Nowak",
#       "email": "anna@example.com"
#     }
#   }
# }