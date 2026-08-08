# Zadanie 16 – Chat z historią
# Rozszerz chat server o zapisywanie historii wiadomości do bazy danych (SQLite) i
# wysyłanie ostatnich 50 wiadomości przy połączeniu nowego klienta.



import aiohttp
from aiohttp import web
import sqlite3
import asyncio
from typing import Set

# Zbiór aktywnych połączeń
active_connections: Set[web.WebSocketResponse] = set()

# Funkcja inicjalizująca moją bazę danych
def init_db():
    """Tworzę plik bazy i tabelę, jeśli jeszcze nie istnieją"""
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Baza danych SQLite została zainicjalizowana.")

# Synchroniczna funkcja do pobierania historii (uruchomię ją w tle)
def get_last_50_messages():
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    # Pobieram 50 ostatnich wiadomości, sortując malejąco po ID
    cursor.execute('SELECT text FROM messages ORDER BY id DESC LIMIT 50')
    rows = cursor.fetchall()
    conn.close()
    
    # Odwracam listę, żeby najstarsze z tych 50 wiadomości wyświetliły się jako pierwsze
    return [row[0] for row in reversed(rows)]

# Synchroniczna funkcja do zapisywania nowej wiadomości (uruchomię ją w tle)
def save_message(text: str):
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO messages (text) VALUES (?)', (text,))
    conn.commit()
    conn.close()

async def chat_handler(request):
    """Handler obsługujący czat z historią z bazy danych"""
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    
    # Dodaję klienta do aktywnych połączeń
    active_connections.add(ws)
    print(f"Nowy klient! Łącznie połączeń: {len(active_connections)}")
    
    # KROK 1: Pobieram historię z bazy (asynchronicznie) i wysyłam do klienta
    history = await asyncio.to_thread(get_last_50_messages)
    
    if history:
        await ws.send_str("--- Ostatnie wiadomości na serwerze ---")
        for msg in history:
            await ws.send_str(msg)
        await ws.send_str("--- Koniec historii ---")
    else:
        await ws.send_str("--- Historia jest pusta. Bądź pierwszy! ---")

    try:
        # KROK 2: Nasłuchuję nowych wiadomości
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                user_message = msg.data
                print(f"Otrzymano i zapisuję: {user_message}")
                
                # Zapisuję wiadomość do bazy SQLite (w tle, bez blokowania serwera)
                await asyncio.to_thread(save_message, user_message)
                
                # Rozsyłam nową wiadomość do wszystkich podłączonych klientów
                for conn in active_connections:
                    await conn.send_str(user_message)
                    
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print(f"Błąd WebSocket: {ws.exception()}")
                
    finally:
        # Usuwam klienta po rozłączeniu[cite: 1]
        active_connections.discard(ws)
        print(f"Klient rozłączony. Zostało: {len(active_connections)}")
        
    return ws

# Inicjalizuję bazę przy starcie pliku
init_db()

app = web.Application()
app.router.add_get('/chat', chat_handler)

if __name__ == '__main__':
    print("Mój serwer czatu z historią działa na ws://localhost:8080/chat")
    web.run_app(app, host='localhost', port=8080)