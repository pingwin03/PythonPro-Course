# Zadanie 15 – GraphQL Subscription
# Zaimplementuj GraphQL subscription (używając WebSocket pod spodem), która emituje
# event gdy nowy użytkownik się zarejestruje.
# Pomoc: użyj strawberry.subscription i AsyncGenerator 



import asyncio
import strawberry
from typing import AsyncGenerator, List
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView

# Mój typ reprezentujący nowo zarejestrowanego użytkownika
@strawberry.type
class User:
    name: str

# Tworzę globalną listę kolejek dla wszystkich aktywnych subskrybentów
# Każdy, kto nasłuchuje, dostanie tu swoją kolejkę
subscribers: List[asyncio.Queue] = []

@strawberry.type
class Query:
    # Strawberry wymaga, aby istniało przynajmniej jedno podstawowe zapytanie
    @strawberry.field
    def hello(self) -> str:
        return "Cześć! Użyj mutacji i subskrypcji."

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def register_user(self, name: str) -> User:
        """Rejestruję użytkownika i powiadamiam subskrybentów"""
        new_user = User(name=name)
        
        print(f"Zarejestrowano nowego użytkownika: {name}. Powiadamiam {len(subscribers)} subskrybentów!")
        
        # Wysyłam obiekt nowego użytkownika do każdej aktywnej kolejki
        for queue in subscribers:
            await queue.put(new_user)
            
        return new_user

@strawberry.type
class Subscription:
    # Zgodnie z podpowiedzią używam dekoratora i typu AsyncGenerator
    @strawberry.subscription
    async def user_registered(self) -> AsyncGenerator[User, None]:
        """Nasłuchuję na nowe rejestracje"""
        # Tworzę nową kolejkę dla tego konkretnego klienta
        queue = asyncio.Queue()
        subscribers.append(queue)
        print("Nowy klient zasubskrybował zdarzenia rejestracji!")
        
        try:
            # Pętla nieskończona, która czeka na pojawienie się danych w kolejce
            while True:
                # Usypiam tę pętlę do momentu, aż w kolejce pojawi się nowy użytkownik
                user = await queue.get()
                # Yield ("zwraca" i pauzuje) wysyła dane do klienta przez WebSocket
                yield user
        finally:
            # Gdy klient się rozłączy, usuwam jego kolejkę
            subscribers.remove(queue)
            print("Klient anulował subskrypcję.")

# Tworzę schemat z wszystkimi trzema elementami: Query, Mutation i Subscription
schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)

app = web.Application()
# GraphQLView w Strawberry domyślnie potrafi obsłużyć WebSockets dla subskrypcji
app.router.add_route("*", "/graphql", GraphQLView(schema=schema))

if __name__ == '__main__':
    print("Mój serwer GraphQL z subskrypcjami działa na http://localhost:8000/graphql")
    web.run_app(app, host='localhost', port=8000)