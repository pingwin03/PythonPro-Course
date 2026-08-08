# Zadanie 18 – Real-time notifications
# Stwórz system powiadomień: aplikacja ma REST API do tworzenia powiadomień oraz
# WebSocket endpoint, który pushuje powiadomienia do zalogowanych użytkowników w
# czasie rzeczywistym.


import aiohttp
from aiohttp import web
from typing import Set

# W tym zbiorze przechowuję aktywne połączenia WebSocket moich zalogowanych użytkowników
active_connections: Set[web.WebSocketResponse] = set()

# 1. Mój endpoint WebSocket (dla klientów, którzy chcą odbierać powiadomienia)
async def websocket_handler(request):
    """Mój kanał WebSocket, który pushuje powiadomienia w czasie rzeczywistym"""
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    
    # Dodaję nowego klienta do mojego zbioru
    active_connections.add(ws)
    print(f"Nowy klient nasłuchuje powiadomień. Aktywnych połączeń: {len(active_connections)}")
    
    try:
        # Czekam na ewentualne komunikaty od klienta (choć w tym scenariuszu klient głównie słucha)
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.ERROR:
                print(f"Błąd połączenia: {ws.exception()}")
    finally:
        # Usuwam klienta, gdy zamknie aplikację
        active_connections.discard(ws)
        print(f"Klient odłączył się. Zostało połączeń: {len(active_connections)}")
        
    return ws

# 2. Mój endpoint REST API (do tworzenia nowych powiadomień)
async def create_notification(request):
    """Endpoint REST, który przyjmuje dane JSON i rozsyła je do klientów WS"""
    try:
        # Oczekuję danych w formacie JSON
        data = await request.json()
        message = data.get("message")
        
        # Sprawdzam, czy otrzymałem treść powiadomienia
        if not message:
            return web.json_response({"error": "Brak pola 'message' w żądaniu JSON"}, status=400)
            
        print(f"REST API: Otrzymałem polecenie wysłania powiadomienia: '{message}'")
        
        # Wypycham (push) powiadomienie do wszystkich aktywnych połączeń WebSocket
        for conn in active_connections:
            await conn.send_json({"notification": message})
            
        # Zwracam odpowiedź HTTP potwierdzającą sukces
        return web.json_response({
            "status": "Powiadomienie zostało wypchnięte pomyślnie", 
            "delivered_to_clients": len(active_connections)
        })
        
    except Exception as e:
        return web.json_response({"error": f"Błąd serwera: {str(e)}"}, status=500)

# Konfiguruję i uruchamiam aplikację
app = web.Application()

# Rejestruję dwie różne ścieżki i metody
app.router.add_get('/ws/notifications', websocket_handler)
app.router.add_post('/api/notifications', create_notification)

if __name__ == '__main__':
    print("Mój hybrydowy system powiadomień jest uruchomiony!")
    print(" -> Klienci nasłuchują na: ws://localhost:8080/ws/notifications")
    print(" -> Tworzenie powiadomień: POST http://localhost:8080/api/notifications")
    web.run_app(app, host='localhost', port=8080)