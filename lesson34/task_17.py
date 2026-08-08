import asyncio
import strawberry
from strawberry.dataloader import DataLoader
from typing import List, Optional
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView

# Przygotowuję moje "fałszywe" bazy danych
@strawberry.type
class Post:
    id: int
    title: str
    author_id: int

class DBUser:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

fake_users_db = [
    DBUser(id=1, name="Jan Kowalski"),
    DBUser(id=2, name="Anna Nowak"),
    DBUser(id=3, name="Piotr Wiśniewski"),
]

fake_posts_db = [
    Post(id=1, title="Mój pierwszy post", author_id=1),
    Post(id=2, title="Wprowadzenie do DataLoadera", author_id=1),
    Post(id=3, title="Asynchroniczność w Pythonie", author_id=2),
    Post(id=4, title="GraphQL vs REST", author_id=3),
]

# Funkcja grupująca dla DataLoadera
async def load_posts_by_author_ids(keys: List[int]) -> List[List[Post]]:
    print(f"\n---> UWAGA: DataLoader pobiera posty HURTOWO dla autorów o ID: {keys} <---")
    
    posts_by_author = {key: [] for key in keys}
    for post in fake_posts_db:
        if post.author_id in keys:
            posts_by_author[post.author_id].append(post)
            
    return [posts_by_author[key] for key in keys]

@strawberry.type
class User:
    id: int
    name: str

    @strawberry.field
    async def posts(self, info: strawberry.Info) -> List[Post]:
        # Pobieram posty używając DataLoadera z kontekstu
        return await info.context["post_loader"].load(self.id)

@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> List[User]:
        return [User(id=u.id, name=u.name) for u in fake_users_db]

# NOWE ROZWIĄZANIE: Własna klasa widoku zamiast problematycznego argumentu context_getter
class MyGraphQLView(GraphQLView):
    async def get_context(self, request: web.Request, response: web.StreamResponse) -> dict:
        return {
            "post_loader": DataLoader(load_fn=load_posts_by_author_ids)
        }

# Tworzę schemat
schema = strawberry.Schema(query=Query)

# Przygotowuję aplikację
app = web.Application()

# Przekazuję instancję mojej nowej klasy MyGraphQLView
app.router.add_route("*", "/graphql", MyGraphQLView(schema=schema))

if __name__ == '__main__':
    print("Mój serwer z DataLoaderem działa na http://localhost:8000/graphql")
    web.run_app(app, host='localhost', port=8000)