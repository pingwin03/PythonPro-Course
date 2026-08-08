# Zadanie 1 – Prosty echo server
# Stwórz prosty serwer WebSocket, który zwraca każdą otrzymaną wiadomość z dodanym
# prefixem "Server: ".

from aiohttp import web

async def websocket_handler(request):
    # Tworzę nowe połączenie WebSocket
    ws = web.WebSocketResponse()
    
    # Wykonuję handshake, czyli uaktualniam protokół z HTTP do WebSocket
    await ws.prepare(request)
    print("Nowy klient połączył się z moim serwerem!")
    
    # Rozpoczynam nieskończoną pętlę, w której nasłuchuję wiadomości od klienta
    async for msg in ws:
        # Sprawdzam, czy otrzymana wiadomość jest typu tekstowego
        if msg.type == web.WSMsgType.TEXT:
            print(f"Otrzymałem wiadomość: {msg.data}")
            
            # Odsyłam wiadomość z powrotem, dodając wymagany prefiks "Server: "
            await ws.send_str(f"Server: {msg.data}")
            
        # Obsługuję ewentualne błędy połączenia
        elif msg.type == web.WSMsgType.ERROR:
            print(f"Wystąpił błąd w moim połączeniu WebSocket: {ws.exception()}")
            
    print("Mój klient został rozłączony.")
    return ws

# Tworzę instancję aplikacji
app = web.Application()

# Rejestruję endpoint dla mojego serwera WebSocket
app.router.add_get('/ws', websocket_handler)

if __name__ == '__main__':
    print("Uruchamiam mój serwer WebSocket na ws://localhost:8080/ws")
    web.run_app(app, host='localhost', port=8080)
    
    
