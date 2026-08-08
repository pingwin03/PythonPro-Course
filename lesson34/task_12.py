# Zadanie 12 – GraphQL z filtrowaniem
# Rozszerz API z zadania 10 o query posts(authorId: ID) filtrujące posty po autorze oraz
# searchUsers(name: String) wyszukujące użytkowników.

import strawberry
from typing import List, Optional
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView

# Moje "fałszywe" bazy danych
fake_users_db = []
fake_posts_db = []

@strawberry.type
class Post:
    id: int
    title: str
    content: str
    author_id: int

    @strawberry.field
    def author(self) -> Optional['User']:
        for user in fake_users_db:
            if user.id == self.author_id:
                return user
        return None

@strawberry.type
class User:
    id: int
    name: str
    email: str

    @strawberry.field
    def posts(self) -> List[Post]:
        return [post for post in fake_posts_db if post.author_id == self.id]

# Wypełniam bazę danymi
fake_users_db.extend([
    User(id=1, name="Jan Kowalski", email="jan@example.com"),
    User(id=2, name="Anna Nowak", email="anna@example.com"),
    User(id=3, name="Janusz Tracz", email="janusz@example.com"),
])

fake_posts_db.extend([
    Post(id=1, title="Mój pierwszy post", content="Treść pierwszego posta", author_id=1),
    Post(id=2, title="Nauka GraphQL", content="GraphQL jest super!", author_id=1),
    Post(id=3, title="Python i relacje", content="Jak łączyć dane...", author_id=2),
])

# Moje zapytania (Queries)
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

    # NOWOŚĆ: Zapytanie posts z opcjonalnym filtrowaniem po authorId
    @strawberry.field
    def posts(self, author_id: Optional[strawberry.ID] = None) -> List[Post]:
        """Zwracam posty, ewentualnie filtrując je po autorze"""
        if author_id is not None:
            # Rzutuję na int, aby móc porównać z author_id w bazie
            target_id = int(author_id)
            return [post for post in fake_posts_db if post.author_id == target_id]
        
        # Jeśli nie przekazano author_id, zwracam wszystkie
        return fake_posts_db

    # NOWOŚĆ: Wyszukiwanie użytkowników po nazwie
    @strawberry.field
    def search_users(self, name: str) -> List[User]:
        """Wyszukuję użytkowników, których imię zawiera podany fragment"""
        # Używam lower(), aby wyszukiwanie nie zważało na wielkość liter
        search_query = name.lower()
        return [user for user in fake_users_db if search_query in user.name.lower()]

# Tworzę schemat
schema = strawberry.Schema(query=Query)

# Przygotowuję aplikację
app = web.Application()
app.router.add_route("*", "/graphql", GraphQLView(schema=schema))

if __name__ == '__main__':
    print("Moje API GraphQL z filtrowaniem działa na http://localhost:8000/graphql")
    web.run_app(app, host='localhost', port=8000)