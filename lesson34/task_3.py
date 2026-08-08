# Zadanie 3 – Licznik połączeń
# Zmodyfikuj echo server tak, aby przy każdym nowym połączeniu wysyłał wiadomość
# "Jesteś klientem numer X", gdzie X to liczba aktywnych połączeń.


from aiohttp import web
from typing import Set

# Tworzę globalny zbiór, w którym będę przechowywać wszystkie moje aktywne połączenia
active_connections: Set[web.WebSocketResponse] = set()

async def websocket_handler(request):
    # Przygotowuję nowe połączenie WebSocket
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    
    # Dodaję nowe połączenie do mojego zbioru aktywnych połączeń
    active_connections.add(ws)
    
    # Obliczam numer klienta na podstawie wielkości zbioru
    client_number = len(active_connections)
    print(f"Nowy klient połączył się z moim serwerem! Łącznie połączeń: {client_number}")
    
    # Wysyłam nowemu klientowi informację, którym jest z kolei
    await ws.send_str(f"Jesteś klientem numer {client_number}")
    
    try:
        # Rozpoczynam nasłuchiwanie wiadomości (mój echo serwer z zadania 1)
        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                print(f"Otrzymałem wiadomość od klienta nr {client_number}: {msg.data}")
                # Odsyłam echo z prefiksem
                await ws.send_str(f"Server: {msg.data}")
                
            elif msg.type == web.WSMsgType.ERROR:
                print(f"Wystąpił błąd w moim połączeniu: {ws.exception()}")
                
    finally:
        # Ten blok wykona się zawsze, gdy klient się rozłączy
        # Usuwam zamknięte połączenie z mojego zbioru aktywnych klientów
        active_connections.discard(ws)
        print(f"Klient rozłączony. Zostało aktywnych połączeń: {len(active_connections)}")
        
    return ws

# Przygotowuję i uruchamiam moją aplikację
app = web.Application()
app.router.add_get('/ws', websocket_handler)

if __name__ == '__main__':
    print("Uruchamiam mój serwer WebSocket z licznikiem połączeń na ws://localhost:8080/ws")
    web.run_app(app, host='localhost', port=8080)
    
# Test:

# Zatrzymuję stary serwer (np. za pomocą skrótu Ctrl+C w konsoli) i uruchamiam ten nowy skrypt (task_3.py).

# Mogę uruchomić klienta z Zadania 2 (task_2.py) w osobnym oknie terminala. 
# Jako pierwszą odpowiedź otrzyma on moją wiadomość: "Jesteś klientem numer 1".

# Jeśli otworzę jeszcze jeden terminal i uruchomię w nim kolejnego klienta, on dostanie wiadomość 
# "Jesteś klientem numer 2", podczas gdy jedynka będzie nadal podłączona! 
# Po zakończeniu skryptu klienta, na serwerze zobaczę, że liczba połączeń znów spadła.



# terminal 1:
#    PS E:\PythonPro-Course\homework\lesson34> & C:\Users\pingw\AppData\Local\Programs\Python\Python314\python.exe e:/PythonPro-Course/homework/lesson34/task_3.py
# Uruchamiam mój serwer WebSocket z licznikiem połączeń na ws://localhost:8080/ws
# ======== Running on http://localhost:8080 ========
# (Press CTRL+C to quit)
# Nowy klient połączył się z moim serwerem! Łącznie połączeń: 1
# Otrzymałem wiadomość od klienta nr 1: Cześć
# Otrzymałem wiadomość od klienta nr 1: Jak się masz?
# Otrzymałem wiadomość od klienta nr 1: Do widzenia
# Klient rozłączony. Zostało aktywnych połączeń: 0 

# Terminal 2:
# PS E:\PythonPro-Course\homework\lesson34> python task_2.py
# Udało mi się połączyć z serwerem!
# Wysłałem: Cześć
# Otrzymałem odpowiedź: Jesteś klientem numer 1
# Wysłałem: Jak się masz?
# Otrzymałem odpowiedź: Server: Cześć
# Wysłałem: Do widzenia
# Otrzymałem odpowiedź: Server: Jak się masz?
# Moje połączenie zostało poprawnie zamknięte.
# PS E:\PythonPro-Course\homework\lesson34> 