# Zadanie 6 – GraphQL Mutation
# Dodaj mutację createUser(name: String!, email: String!) która dodaje użytkownika
# do listy i zwraca go

import strawberry
from typing import Optional, List
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView

# Mój typ GraphQL dla użytkownika
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

# Moje zapytania (Queries) z poprzednich zadań
@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: strawberry.ID) -> Optional[User]:
        for user in fake_users_db:
            if user.id == id:
                return user
        return None

    @strawberry.field
    def users(self) -> List[User]:
        return fake_users_db

# NOWOŚĆ: Definiuję mutacje (Mutations) do modyfikacji danych
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str, email: str) -> User:
        """Tworzę nowego użytkownika, dodaję do bazy i zwracam go"""
        # Znajduję najwyższe obecne ID w mojej bazie, aby wygenerować kolejne
        if fake_users_db:
            max_id = max([int(u.id) for u in fake_users_db])
        else:
            max_id = 0
            
        new_id = strawberry.ID(str(max_id + 1))
        
        # Tworzę nowego użytkownika
        new_user = User(id=new_id, name=name, email=email)
        
        # Dodaję go do mojej listy
        fake_users_db.append(new_user)
        
        return new_user

# Tworzę mój schemat, dodając do niego zarówno Query, jak i Mutation
schema = strawberry.Schema(query=Query, mutation=Mutation)

# Przygotowuję i uruchamiam aplikację
app = web.Application()
app.router.add_route("*", "/graphql", GraphQLView(schema=schema))

if __name__ == '__main__':
    print("Moje API GraphQL działa na http://localhost:8000/graphql")
    web.run_app(app, host='localhost', port=8000)
    
    
# test:
    
# Zapisuję kod, uruchamiam skrypt i wchodzę na adres 
# http://localhost:8000/graphql.
# Aby dodać użytkownika, używam słowa kluczowego mutation i wywołuję moją funkcję.
# Wpisuję w interfejsie po lewej stronie następujące zapytanie 
# (które jest bardzo podobne do tego z materiałów z lekcji): 

# mutation {
#   createUser(name: "Michał Testowy", email: "michal@example.com") {
#     id
#     name
#     email
#   }
# }
# Po wciśnięciu przycisku "Play", po prawej stronie widze  odpowiedź z nowo wygenerowanym ID 
# z przypisanymi danymi.Mogę to dodatkowo zweryfikować! Jeśli teraz wrócę do zwykłego zapytania query 
# { users { id name } } i je wywołam, na liście zwracanych użytkownikówobaczę nowo dodaną osobę, 
# co oznacza, że moja mutacja trwale zmodyfikowała działającą w tle strukturę danych.

# {
#   "data": {
#     "createUser": {
#       "id": "4",
#       "name": "Michał Testowy",
#       "email": "michal@example.com"
#     }
#   }
# }