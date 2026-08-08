# Zadanie 10 – GraphQL z relacjami
# Stwórz API z typami User i Post , gdzie User ma pole posts zwracające listę jego
# postów, oraz Post ma pole author zwracające autora.


import strawberry
from typing import List, Optional
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView

# Najpierw tworzę puste listy na moje dane, aby resolvery w klasach miały do nich dostęp
fake_users_db = []
fake_posts_db = []

# Definiuję typ Post
@strawberry.type
class Post:
    id: int
    title: str
    content: str
    author_id: int

    # Definiuję pole relacji: Post ma jednego autora
    @strawberry.field
    def author(self) -> Optional['User']:
        """Szukam i zwracam autora tego posta"""
        for user in fake_users_db:
            if user.id == self.author_id:
                return user
        return None

# Definiuję typ User
@strawberry.type
class User:
    id: int
    name: str
    email: str

    # Definiuję pole relacji: User ma listę postów
    @strawberry.field
    def posts(self) -> List[Post]:
        """Szukam i zwracam wszystkie posty należące do mnie (do tego użytkownika)"""
        # Używam list comprehension, by przefiltrować posty po moim ID[cite: 1]
        return [post for post in fake_posts_db if post.author_id == self.id]

# Wypełniam moją bazę przykładowymi danymi[cite: 1]
fake_users_db.extend([
    User(id=1, name="Jan Kowalski", email="jan@example.com"),
    User(id=2, name="Anna Nowak", email="anna@example.com"),
])

fake_posts_db.extend([
    Post(id=1, title="Mój pierwszy post", content="Treść pierwszego posta", author_id=1),
    Post(id=2, title="Nauka GraphQL", content="GraphQL jest super!", author_id=1),
    Post(id=3, title="Python i relacje", content="Jak łączyć dane...", author_id=2),
])

# Definiuję główne zapytania mojego API
@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: int) -> Optional[User]:
        for user in fake_users_db:
            if user.id == id:
                return user
        return None

    @strawberry.field
    def post(self, id: int) -> Optional[Post]:
        for post in fake_posts_db:
            if post.id == id:
                return post
        return None
        
    @strawberry.field
    def users(self) -> List[User]:
        return fake_users_db

# Tworzę schemat
schema = strawberry.Schema(query=Query)

# Konfiguruję i uruchamiam serwer aiohttp
app = web.Application()
# Pamiętam, aby użyć wersji bez graphiql=True
app.router.add_route("*", "/graphql", GraphQLView(schema=schema))

if __name__ == '__main__':
    print("Moje API GraphQL z relacjami działa na http://localhost:8000/graphql")
    web.run_app(app, host='localhost', port=8000)
    
    
# test:
    
# python task_10.py
# Otwieram przeglądarkę pod adresem http://localhost:8000/graphql

# wpisuje:query {
#   user(id: 1) {
#     name
#     email
#     posts {
#       title
#       content
#     }
#   }
# }

# odpowiedź:
#     {
#   "data": {
#     "user": {
#       "name": "Jan Kowalski",
#       "email": "jan@example.com",
#       "posts": [
#         {
#           "title": "Mój pierwszy post",
#           "content": "Treść pierwszego posta"
#         },
#         {
#           "title": "Nauka GraphQL",
#           "content": "GraphQL jest super!"
#         }
#       ]
#     }
#   }
# }



# pytanie:
    
# query {
#   post(id: 3) {
#     title
#     author {
#       name
#     }
#   }
# }


# odpowiedż:
    
# {
#   "data": {
#     "post": {
#       "title": "Python i relacje",
#       "author": {
#         "name": "Anna Nowak"
#       }
#     }
#   }
# }