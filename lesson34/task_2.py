# Zadanie 2 – Klient wysyłający 3 wiadomości
# Napisz klienta WebSocket, który łączy się z serwerem i wysyła 3 wiadomości: "Cześć", "Jak
# się masz?", "Do widzenia"


import aiohttp
import asyncio

async def websocket_client():
    # Tworzę sesję HTTP, która jest wymagana do nawiązania połączenia WebSocket
    async with aiohttp.ClientSession() as session:
        # Łączę się z moim serwerem WebSocket pod adresem z poprzedniego zadania
        async with session.ws_connect('ws://localhost:8080/ws') as ws:
            print("Udało mi się połączyć z serwerem!")
            
            # Przygotowuję listę 3 wymaganych w zadaniu wiadomości
            messages = ["Cześć", "Jak się masz?", "Do widzenia"]
            
            for msg in messages:
                # Wysyłam kolejną wiadomość tekstową do serwera
                await ws.send_str(msg)
                print(f"Wysłałem: {msg}")
                
                # Czekam na odpowiedź od serwera (echo z prefiksem)
                response = await ws.receive()
                
                # Sprawdzam, czy odpowiedź jest tekstem i ją wyświetlam
                if response.type == aiohttp.WSMsgType.TEXT:
                    print(f"Otrzymałem odpowiedź: {response.data}")
                    
                # Robię małą, jednosekundową pauzę przed wysłaniem kolejnej wiadomości
                await asyncio.sleep(1)
                
            # Po wysłaniu i odebraniu wszystkich wiadomości, zamykam moje połączenie
            await ws.close()
            print("Moje połączenie zostało poprawnie zamknięte.")

if __name__ == '__main__':
    # Uruchamiam moją asynchroniczną pętlę dla klienta
    asyncio.run(websocket_client())
    
    
# Test:
#     Jak to przetestuję?
#     Krok 1: Upewniam się, że w jednym oknie terminala działa mój skrypt z Zadania 1 (serwer).
#     Krok 2: Zapisuję powyższy kod w task_2.py.
#     Krok 3: Otwieram drugie okno terminala i uruchamiam w nim mojego klienta wpisując:
#         python task_2.py.
#     Krok 4: W oknie klienta widzę wysyłane przeze mnie wiadomości oraz 
#     odpowiedzi z prefiksem Server: . Z kolei w oknie serwera widzę logi o nowym połączeniu
#     i otrzymanych ode mnie wiadomościach tekstowych.  


# PS E:\PythonPro-Course\homework\lesson34> python task_2.py
# Udało mi się połączyć z serwerem!
# Wysłałem: Cześć
# Otrzymałem odpowiedź: Server: Cześć
# Wysłałem: Jak się masz?
# Otrzymałem odpowiedź: Server: Jak się masz?
# Wysłałem: Do widzenia
# Otrzymałem odpowiedź: Server: Do widzenia
# Moje połączenie zostało poprawnie zamknięte.
# PS E:\PythonPro-Course\homework\lesson34> 




# PS E:\PythonPro-Course\homework\lesson34> & C:\Users\pingw\AppData\Local\Programs\Python\Python314\python.exe e:/PythonPro-Course/homework/lesson34/task_1.py
# Uruchamiam mój serwer WebSocket na ws://localhost:8080/ws
# ======== Running on http://localhost:8080 ========
# (Press CTRL+C to quit)
# Nowy klient połączył się z moim serwerem!
# Otrzymałem wiadomość: Cześć
# Otrzymałem wiadomość: Jak się masz?
# Otrzymałem wiadomość: Do widzenia
# Mój klient został rozłączony.
