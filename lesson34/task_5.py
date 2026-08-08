# Zadanie 5 – GraphQL - Lista użytkowników
# Rozszerz API z zadania 4 o query users zwracające listę wszystkich użytkowników.

import strawberry
from typing import Optional, List
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView

# Definiuję mój typ GraphQL dla użytkownika
@strawberry.type
class User:
    id: strawberry.ID
    name: str
    email: str

# Moja "fałszywa" baza danych
fake_users_db = [
    User(id=strawberry.ID("1"), name="Jan Kowalski", email="jan@example.com"),
    User(id=strawberry.ID("2"), name="Anna Nowak", email="anna@example.com"),
    User(id=strawberry.ID("3"), name="Piotr Wiśniewski", email="piotr@example.com"),
]

# Definiuję główne zapytania (Queries)
@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: strawberry.ID) -> Optional[User]:
        """Szukam i pobieram pojedynczego użytkownika po ID"""
        for user in fake_users_db:
            if user.id == id:
                return user
        return None

    # NOWOŚĆ: Dodaję nowe zapytanie zwracające listę wszystkich użytkowników
    @strawberry.field
    def users(self) -> List[User]:
        """Pobieram wszystkich użytkowników z mojej bazy"""
        return fake_users_db

# Tworzę mój schemat
schema = strawberry.Schema(query=Query)

# Przygotowuję aplikację
app = web.Application()
# Pamiętam, żeby nie używać parametru graphiql=True, tak jak ustaliliśmy wcześniej
app.router.add_route("*", "/graphql", GraphQLView(schema=schema))

if __name__ == '__main__':
    print("Moje API GraphQL działa na http://localhost:8000/graphql")
    web.run_app(app, host='localhost', port=8000)
    
    
    
# test:
    
# Uruchamiam ponownie mój zaktualizowany skrypt.
# Otwieram adres http://localhost:8000/graphql w przeglądarce.
# Wpisuję po lewej stronie nowe zapytanie, które pobierze wszystkich użytkowników bez podawania żadnego ID: 
# GraphQLquery {
#   users {
#     id
#     name
#     email
#   }
# }
# Po kliknięciu przycisku uruchamiania, po prawej stronie widze listę (tablicę JSON) 
# zawierającą dane Jana, Anny oraz Piotra! Zgodnie z założeniami GraphQL,
# otrzymam dokładnie te dane, o które poprosiłem w zapytaniu

# {
#   "data": {
#     "users": [
#       {
#         "id": "1",
#         "name": "Jan Kowalski",
#         "email": "jan@example.com"
#       },
#       {
#         "id": "2",
#         "name": "Anna Nowak",
#         "email": "anna@example.com"
#       },
#       {
#         "id": "3",
#         "name": "Piotr Wiśniewski",
#         "email": "piotr@example.com"
#       }
#     ]
#   }
# }