# Zadanie 8 – Pomiar czasu połączenia
# Zmodyfikuj WebSocket handler, aby mierzył czas połączenia każdego klienta (od connect
# do disconnect) i wyświetlał go.


import time
from aiohttp import web
import aiohttp

async def websocket_handler(request):
    """Mój handler z pomiarem czasu połączenia"""
    ws = web.WebSocketResponse()
    
    # Akceptuję żądanie i uaktualniam protokół do WebSocket
    await ws.prepare(request)
    
    # Zapisuję czas startu zaraz po pomyślnym połączeniu
    start_time = time.time()
    print("Nowy klient połączony! Rozpoczynam pomiar czasu...")
    
    try:
        # Pętla nasłuchiwania wiadomości od klienta
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                print(f"Otrzymałem: {msg.data}")
                # Odsyłam proste echo, żeby klient widział, że serwer działa
                await ws.send_str(f"Otrzymano: {msg.data}")
                
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print(f"Wystąpił błąd WebSocket: {ws.exception()}")
                
    finally:
        # Ten blok uruchomi się, gdy klient się rozłączy (np. zamknie terminal)
        end_time = time.time()
        
        # Obliczam czas trwania połączenia w sekundach
        connection_duration = end_time - start_time
        
        # Wyświetlam wynik, zaokrąglając go do dwóch miejsc po przecinku dla czytelności
        print(f"Klient został rozłączony. Czas połączenia wynosił: {connection_duration:.2f} sekund.")
        
    return ws

# Konfiguruję i uruchamiam moją aplikację
app = web.Application()
app.router.add_get('/ws', websocket_handler)

if __name__ == '__main__':
    print("Mój serwer z pomiarem czasu działa na ws://localhost:8080/ws")
    web.run_app(app, host='localhost', port=8080)
    
    
#   Test  
# 1. Zapisuję mój nowy skrypt (np. jako task_8.py) i uruchamiam go w głównym oknie terminala.

# 2. Otwieram drugie okno terminala, tak jak zrobiłem to w poprzednim zadaniu, 
# i uruchamiam mojego klienta (np. task_2.py).

# 3. Zauważę, że po połączeniu serwer wyświetli komunikat 
# "Nowy klient połączony! Rozpoczynam pomiar czasu...".

# 4. Mój klient wyśle trzy wiadomości z jednosekundowymi przerwami, po czym automatycznie
# zamknie połączenie.

# 5. W tym momencie na serwerze uruchomi się mój blok finally i widzę podsumowanie, 
# np.: "Klient został rozłączony. Czas połączenia wynosił: 3.05 sekund."