import aiohttp
import asyncio
import jwt

# Używam tego samego klucza, co na serwerze!
SECRET_KEY = "moj_super_tajny_klucz"

async def secure_client():
    # 1. Najpierw generuję ważny token dla mojego użytkownika
    my_token = jwt.encode({"user_id": "Pingwin"}, SECRET_KEY, algorithm="HS256")
    
    # 2. Tworzę celowo nieprawidłowy token dla testu (zakomentowany)
    # my_token = "jakis.falszywy.token"
    
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect('ws://localhost:8080/ws') as ws:
            print(f"Połączyłem się! Wysyłam mój token JWT...")
            
            # Najpierw wysyłam wygenerowany token[cite: 1]
            await ws.send_str(my_token)
            
            # Czekam na weryfikację od serwera
            auth_response = await ws.receive()
            if auth_response.type == aiohttp.WSMsgType.TEXT:
                print(f"Serwer: {auth_response.data}")
                
                # Jeśli serwer mnie wpuścił, wysyłam tajne informacje
                if "udana" in auth_response.data:
                    await asyncio.sleep(1)
                    print("Wysyłam moją tajną wiadomość...")
                    await ws.send_str("To jest bardzo tajny raport systemowy.")
                    
                    final_response = await ws.receive()
                    if final_response.type == aiohttp.WSMsgType.TEXT:
                        print(f"Serwer: {final_response.data}")

if __name__ == '__main__':
    asyncio.run(secure_client())