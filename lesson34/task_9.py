# Zadanie 9 – Chat z nickami
# Stwórz chat room, gdzie pierwsza wiadomość od klienta to jego nick, a kolejne to
# wiadomości broadcastowane jako "Nick: wiadomość".

import aiohttp
from aiohttp import web
from typing import Set

# W tym zbiorze przechowuję wszystkie aktywne połączenia WebSocket
active_connections: Set[web.WebSocketResponse] = set()

async def chat_handler(request):
    """Mój handler obsługujący czat z nickami"""
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    
    # Dodaję nowe połączenie do zbioru aktywnych[cite: 1]
    active_connections.add(ws)
    
    # Inicjalizuję zmienną na nick dla tego konkretnego klienta
    nickname = None
    
    try:
        # Nasłuchuję wiadomości[cite: 1]
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                # Jeśli klient nie ma jeszcze nicku, to pierwsza wiadomość nim zostaje
                if nickname is None:
                    nickname = msg.data
                    print(f"Nowy użytkownik dołączył i ustawił nick: {nickname}")
                    
                    # Powiadamiam wszystkich o dołączeniu nowej osoby
                    for conn in active_connections:
                        await conn.send_str(f"--- Użytkownik {nickname} dołączył do czatu ---")
                else:
                    # Skoro nick jest już ustawiony, traktuję to jako zwykłą wiadomość
                    chat_message = f"{nickname}: {msg.data}"
                    print(f"Rozsyłam: {chat_message}")
                    
                    # Wykonuję broadcast do wszystkich podłączonych[cite: 1]
                    for conn in active_connections:
                        await conn.send_str(chat_message)
                        
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print(f"Błąd połączenia dla {nickname}: {ws.exception()}")
                
    finally:
        # Użytkownik się rozłącza, więc usuwam go z listy[cite: 1]
        active_connections.discard(ws)
        if nickname:
            print(f"Użytkownik {nickname} opuścił czat.")
            # Informuję pozostałych, że ktoś wyszedł
            for conn in active_connections:
                # Sprawdzam, by nie wysyłać do zamkniętych już połączeń
                if not conn.closed:
                    await conn.send_str(f"--- Użytkownik {nickname} opuścił czat ---")
                    
    return ws

# Konfiguruję i uruchamiam moją aplikację aiohttp[cite: 1]
app = web.Application()
app.router.add_get('/chat', chat_handler)

if __name__ == '__main__':
    print("Mój czat z nickami działa na ws://localhost:8080/chat")
    web.run_app(app, host='localhost', port=8080)