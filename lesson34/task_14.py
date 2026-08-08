# Zadanie 14 – WebSocket z autentykacją
# Zaimplementuj autentykację przez token: klient wysyła token JWT w pierwszej wiadomości,
# serwer weryfikuje i dopiero wtedy akceptuje dalsze wiadomości.


import aiohttp
from aiohttp import web
import jwt

# Ustawiam tajny klucz, którym będę podpisywać i weryfikować moje tokeny
SECRET_KEY = "moj_super_tajny_klucz"

async def auth_handler(request):
    """Mój handler wymagający autentykacji JWT"""
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    
    # Na początku klient jest niezalogowany
    is_authenticated = False
    
    print("Nowy klient połączony. Oczekuję na token JWT...")
    
    try:
        async for msg in ws:
            # Przetwarzam tylko wiadomości tekstowe[cite: 1]
            if msg.type == aiohttp.WSMsgType.TEXT:
                
                # Jeśli klient nie jest jeszcze zautoryzowany, ta wiadomość MUSI być tokenem
                if not is_authenticated:
                    token = msg.data.strip()
                    
                    try:
                        # Próbuję zdekodować i zweryfikować token
                        decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
                        
                        # Jeśli dekodowanie się powiedzie, zmieniam status na zautoryzowany
                        is_authenticated = True
                        user_id = decoded_payload.get("user_id", "Nieznany")
                        
                        print(f"Sukces! Użytkownik '{user_id}' zautoryzowany pomyślnie.")
                        await ws.send_str(f"Autoryzacja udana! Witaj {user_id}. Możesz wysyłać wiadomości.")
                        
                    except jwt.ExpiredSignatureError:
                        print("Odrzucono: Token wygasł.")
                        await ws.send_str("Błąd: Twój token JWT wygasł.")
                        await ws.close()
                        break
                        
                    except jwt.InvalidTokenError:
                        print("Odrzucono: Nieprawidłowy token.")
                        await ws.send_str("Błąd: Nieprawidłowy token JWT.")
                        await ws.close()
                        break
                
                # Jeśli klient JEST już zautoryzowany, normalnie przetwarzam jego wiadomości
                else:
                    print(f"Otrzymałem zabezpieczoną wiadomość: {msg.data}")
                    await ws.send_str(f"Serwer odebrał Twoją wiadomość: {msg.data}")
                    
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print(f"Błąd połączenia: {ws.exception()}")
                
    finally:
        print("Połączenie z klientem zamknięte.")
        
    return ws

app = web.Application()
app.router.add_get('/ws', auth_handler)

if __name__ == '__main__':
    print("Mój zabezpieczony serwer WebSocket działa na ws://localhost:8080/ws")
    web.run_app(app, host='localhost', port=8080)