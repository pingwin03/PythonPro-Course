# Zadanie 7 – WebSocket broadcast podstawowy
# Stwórz serwer WebSocket, który rozesła otrzymaną wiadomość do wszystkich
# podłączonych klientów (broadcast).

import aiohttp
from aiohttp import web

# Tutaj będę przechowywać wszystkie aktywne obiekty WebSocket
active_connections = set()

async def websocket_handler(request):
    """Mój handler obsługujący połączenia WebSocket"""
    ws = web.WebSocketResponse()
    
    # Akceptuję nowe połączenie
    await ws.prepare(request)
    
    # Dodaję nowego klienta do mojego zbioru aktywnych połączeń
    active_connections.add(ws)
    print(f"Nowy klient połączony! Aktualna liczba połączeń: {len(active_connections)}")
    
    try:
        # Nasłuchuję wiadomości od tego konkretnego klienta
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                print(f"Otrzymałem wiadomość: {msg.data}")
                
                # BROADCAST: Rozsyłam wiadomość do wszystkich klientów w moim zbiorze
                for connection in active_connections:
                    # Opcjonalnie mogę pominąć nadawcę sprawdzając: if connection != ws:
                    # Ale na potrzeby tego zadania wyślę ją do wszystkich, 
                    # żeby nadawca też widział potwierdzenie.
                    await connection.send_str(f"Wiadomość do wszystkich: {msg.data}")
                    
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print(f"Połączenie zamknięte z błędem: {ws.exception()}")
    
    finally:
        # Kiedy klient się rozłączy (lub wystąpi błąd), usuwam go z mojego zbioru
        active_connections.remove(ws)
        print(f"Klient rozłączony. Pozostało połączeń: {len(active_connections)}")
        
    return ws

# Konfiguruję i uruchamiam aplikację
app = web.Application()
app.router.add_get('/ws', websocket_handler)

if __name__ == '__main__':
    print("Mój serwer broadcastowy działa na ws://localhost:8080/ws")
    web.run_app(app, host='localhost', port=8080)
    
    
# test: 
    
    
    
    
    
    
    
#     otrzymałem wiadomość: Cześć
# Otrzymałem wiadomość: Jak się masz?
# Nowy klient połączony! Aktualna liczba połączeń: 2
# Otrzymałem wiadomość: Cześć
# Otrzymałem wiadomość: Do widzenia
# Otrzymałem wiadomość: Jak się masz?
# Klient rozłączony. Pozostało połączeń: 1
# Otrzymałem wiadomość: Do widzenia
# Klient rozłączony. Pozostało połączeń: 0