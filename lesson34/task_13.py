# Zadanie 13 – Pokój chatowy z pokojami
# Stwórz system chat rooms, gdzie klienci mogą dołączać do różnych pokoi (np. "/join
# pokój1") i wiadomości są broadcastowane tylko w obrębie pokoju



import aiohttp
from aiohttp import web
from typing import Dict, Set

# Mój słownik pokoi. Domyślnie tworzę pokój "general"
rooms: Dict[str, Set[web.WebSocketResponse]] = {
    "general": set()
}

async def chat_handler(request):
    """Handler obsługujący pokoje chatowe"""
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    
    # Na start przypisuję każdego nowego klienta do pokoju "general"
    current_room = "general"
    rooms[current_room].add(ws)
    
    # Dla uproszczenia (aby skupić się na pokojach) nick to port klienta lub stała nazwa
    nickname = "Użytkownik" 
    
    await ws.send_str(f"Połączono! Jesteś w pokoju '{current_room}'.")
    await ws.send_str("Aby zmienić pokój, wpisz komendę: /join nazwa_pokoju")
    
    try:
        # Pętla nasłuchiwania wiadomości[cite: 1]
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                text = msg.data.strip()
                
                # Sprawdzam, czy klient chce zmienić pokój
                if text.startswith("/join "):
                    # Wyciągam nazwę nowego pokoju z komendy
                    new_room = text.split(" ", 1)[1].strip()
                    
                    if new_room:
                        # 1. Usuwam klienta z obecnego pokoju
                        rooms[current_room].discard(ws)
                        
                        # 2. Tworzę nowy pokój, jeśli taki jeszcze nie istnieje
                        if new_room not in rooms:
                            rooms[new_room] = set()
                            
                        # 3. Przypisuję klienta do nowego pokoju
                        current_room = new_room
                        rooms[current_room].add(ws)
                        
                        await ws.send_str(f"--- Zmieniłeś pokój na: {current_room} ---")
                        print(f"Klient przeszedł do pokoju: {current_room}")
                else:
                    # To zwykła wiadomość, rozsyłam ją TYLKO w obecnym pokoju[cite: 1]
                    broadcast_msg = f"[{current_room}] {nickname}: {text}"
                    print(f"Rozsyłam w pokoju {current_room}: {text}")
                    
                    for conn in rooms[current_room]:
                        # Wysyłam wiadomość do każdego w tym pokoju[cite: 1]
                        await conn.send_str(broadcast_msg)
                        
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print(f"Błąd połączenia: {ws.exception()}")
                
    finally:
        # Obsługa rozłączenia - usuwam klienta z pokoju, w którym się znajdował[cite: 1]
        if current_room in rooms:
            rooms[current_room].discard(ws)
            print(f"Klient opuścił pokój {current_room}.")
            
            # Opcjonalnie: mogę usunąć pokój, jeśli po wyjściu klienta stał się pusty 
            # (i nie jest to domyślny pokój 'general')
            if not rooms[current_room] and current_room != "general":
                del rooms[current_room]
                print(f"Usunięto pusty pokój: {current_room}")
                
    return ws

app = web.Application()
app.router.add_get('/chat', chat_handler)

if __name__ == '__main__':
    print("Mój serwer z pokojami działa na ws://localhost:8080/chat")
    web.run_app(app, host='localhost', port=8080)