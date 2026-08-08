import aiohttp
import asyncio
import sys

async def chat_client(nick):
    async with aiohttp.ClientSession() as session:
        # Pamiętam, aby połączyć się z nowym endpointem /chat[cite: 1]
        async with session.ws_connect('ws://localhost:8080/chat') as ws:
            print(f"Połączyłem się z serwerem! Ustawiam mój nick na: {nick}")
            
            # 1. Wysyłam nick jako pierwszą wiadomość[cite: 1]
            await ws.send_str(nick)
            
            # 2. Czekam sekundę i wysyłam właściwą wiadomość
            await asyncio.sleep(1)
            await ws.send_str("Cześć wszystkim, to moja testowa wiadomość!")
            
            # 3. Przez 10 sekund nasłuchuję, co serwer do mnie odeśle
            print("Nasłuchuję odpowiedzi od innych...")
            try:
                while True:
                    # Czekam na wiadomość z timeoutem 10 sekund
                    msg = await asyncio.wait_for(ws.receive(), timeout=10.0)
                    if msg.type == aiohttp.WSMsgType.TEXT:
                        print(f"Otrzymałem z serwera: {msg.data}")
            except asyncio.TimeoutError:
                print("Czas minął, zamykam moje połączenie.")
            
            await ws.close()

if __name__ == '__main__':
    # Pobieram nick podany przy uruchamianiu skryptu (lub ustawiam domyślny)
    my_nick = sys.argv[1] if len(sys.argv) > 1 else "Gość"
    asyncio.run(chat_client(my_nick))