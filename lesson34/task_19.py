# Zadanie 19 – GraphQL + WebSocket chat
# Połącz GraphQL i WebSocket: użyj GraphQL do pobierania historii chatu, user profiles, oraz
# GraphQL subscriptions do real-time wiadomości.


import asyncio
import strawberry
from typing import List, AsyncGenerator
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView

# 1. Definiuję moje typy danych GraphQL
@strawberry.type
class User:
    id: int
    name: str

@strawberry.type
class Message:
    id: int
    text: str
    author: User

# 2. Tworzę lokalną "bazę danych" i mechanizm kolejek dla subskrypcji
users_db = [
    User(id=1, name="Admin"),
    User(id=2, name="Janek"),
]
messages_db = []
# Lista asynchronicznych kolejek, po jednej dla każdego podłączonego klienta (subskrybenta)
subscribers: List[asyncio.Queue] = []

def get_user_by_id(user_id: int) -> User:
    """Funkcja pomocnicza do wyszukiwania użytkownika"""
    for user in users_db:
        if user.id == user_id:
            return user
    return User(id=user_id, name="Nieznany Użytkownik")

# 3. ZAPYTANIA (Queries) - Służą do pobierania historii i profili
@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> List[User]:
        """Pobieram profile wszystkich użytkowników na serwerze"""
        return users_db

    @strawberry.field
    def history(self) -> List[Message]:
        """Pobieram historię całego czatu"""
        return messages_db

# 4. MUTACJE (Mutations) - Służą do wysyłania wiadomości
@strawberry.type
class Mutation:
    @strawberry.mutation
    async def send_message(self, text: str, author_id: int) -> Message:
        """Tworzę nową wiadomość, zapisuję ją do historii i emituję zdarzenie"""
        author = get_user_by_id(author_id)
        msg_id = len(messages_db) + 1
        
        # Tworzę obiekt nowej wiadomości
        new_msg = Message(id=msg_id, text=text, author=author)
        
        # Zapisuję do historii
        messages_db.append(new_msg)
        print(f"Nowa wiadomość od {author.name}: {text}")
        
        # Wypycham nową wiadomość do wszystkich podłączonych przez WebSocket klientów
        for queue in subscribers:
            await queue.put(new_msg)
            
        return new_msg

# 5. SUBSKRYPCJE (Subscriptions) - Służą do nasłuchiwania w czasie rzeczywistym
@strawberry.type
class Subscription:
    @strawberry.subscription
    async def message_sent(self) -> AsyncGenerator[Message, None]:
        """Nasłuchuję na nowe wiadomości używając asynchronicznego generatora[cite: 1]"""
        # Tworzę prywatną kolejkę dla tego klienta i dodaję ją do globalnej listy
        queue = asyncio.Queue()
        subscribers.append(queue)
        print("Nowy klient podłączył się do strumienia wiadomości (WebSocket)!")
        
        try:
            # W nieskończonej pętli czekam na pojawienie się nowej wiadomości w kolejce
            while True:
                msg = await queue.get()
                yield msg
        finally:
            # Sprzątam, gdy klient opuści czat
            subscribers.remove(queue)
            print("Klient rozłączył się ze strumienia wiadomości.")

# 6. Rejestruję schemat i uruchamiam aplikację webową
schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)

app = web.Application()
# GraphQLView automatycznie zarządza przejściem na WebSocket dla Subscriptions[cite: 1]
app.router.add_route("*", "/graphql", GraphQLView(schema=schema))

if __name__ == '__main__':
    print("Mój hybrydowy chat serwer (GraphQL + WebSocket) działa na http://localhost:8000/graphql")
    web.run_app(app, host='localhost', port=8000)