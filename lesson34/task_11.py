# Zadanie 11 – WebSocket Ping-Pong
# Zaimplementuj mechanizm ping-pong: co 30 sekund serwer wysyła "ping", klient musi
# odpowiedzieć "pong". Jeśli brak odpowiedzi przez 60s, rozłącz klienta



import aiohttp
from aiohttp import web
import asyncio
import time

async def websocket_handler(request):
    """Mój handler z mechanizmem ping-pong"""
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    print("Nowy klient połączony. Zaczynamy zabawę w ping-pong!")

    # Zapisuję czas startu jako pierwszą "aktywność"
    last_pong_time = time.time()

    # Tworzę funkcję, która będzie działać w tle dla tego klienta
    async def heartbeat():
        # Używam nonlocal, aby mieć dostęp do zmiennej z zewnętrznej funkcji
        nonlocal last_pong_time 
        try:
            while not ws.closed:
                # Czekam 30 sekund
                await asyncio.sleep(30)
                
                if ws.closed:
                    break
                
                print("Serwer: Wysyłam 'ping' do klienta...")
                await ws.send_str("ping")
                
                # Sprawdzam, czy minęło więcej niż 60 sekund od ostatniego ponga
                if time.time() - last_pong_time > 60:
                    print("Serwer: Brak odpowiedzi 'pong' przez ponad 60s! Rozłączam klienta.")
                    await ws.close()
                    break
        except asyncio.CancelledError:
            # Ignoruję błąd anulowania zadania, gdy klient sam się rozłączy
            pass

    # Uruchamiam mojego watchdoga w tle
    heartbeat_task = asyncio.create_task(heartbeat())

    try:
        # Główna pętla nasłuchiwania wiadomości od klienta
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                # Sprawdzam typ wiadomości tak, jak sugerowano w lekcji[cite: 1]
                if msg.data == "pong":
                    print("Serwer: Otrzymałem 'pong'! Resetuję licznik czasu.")
                    # Aktualizuję czas ostatniej odpowiedzi
                    last_pong_time = time.time()
                else:
                    print(f"Serwer: Otrzymałem zwykłą wiadomość: {msg.data}")
                    # Przy każdej aktywności również mogę zresetować licznik
                    last_pong_time = time.time()
                    
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print(f"Błąd połączenia: {ws.exception()}")
    finally:
        # Zatrzymuję zadanie w tle, gdy klient się rozłączy
        heartbeat_task.cancel()
        print("Połączenie z klientem zostało zamknięte.")

    return ws

app = web.Application()
app.router.add_get('/ws', websocket_handler)

if __name__ == '__main__':
    print("Mój serwer ping-pong działa na ws://localhost:8080/ws")
    web.run_app(app, host='localhost', port=8080)