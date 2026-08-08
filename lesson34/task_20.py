# Zadanie 20 – Multiplayer game server
# Stwórz prosty serwer gry multiplayer (np. tic-tac-toe lub ping-pong) używając WebSocket.
# Gracze łączą się przez WebSocket, serwer synchronizuje stan gry i rozsyła updaty
# wszystkim graczom.


import aiohttp
from aiohttp import web
import json

# Globalny stan mojej gry
players = {}  # Słownik: obiekt WebSocket -> przypisany znak ('X' lub 'O')
board = [' '] * 9  # Plansza: 9 pustych pól
current_turn = 'X' # Kto ma teraz ruch

# Kombinacje wygrywające na planszy (indeksy 0-8)
WIN_COMBINATIONS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Poziomo
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Pionowo
    [0, 4, 8], [2, 4, 6]              # Skosy
]

def check_winner():
    """Sprawdzam, czy ktoś wygrał lub czy jest remis"""
    for combo in WIN_COMBINATIONS:
        a, b, c = combo
        if board[a] != ' ' and board[a] == board[b] == board[c]:
            return board[a] # Zwracam 'X' lub 'O'
    if ' ' not in board:
        return 'Tie' # Remis
    return None

def reset_game():
    """Resetuję stan planszy do nowej gry"""
    global board, current_turn
    board = [' '] * 9
    current_turn = 'X'
    print("Zresetowałem planszę.")

async def broadcast_state():
    """Rozsyłam aktualny stan gry do wszystkich podłączonych graczy[cite: 1]"""
    winner = check_winner()
    state = {
        "type": "update",
        "board": board,
        "turn": current_turn,
        "winner": winner
    }
    # Używam send_json do automatycznej serializacji danych[cite: 1]
    for ws in players.keys():
        await ws.send_json(state)

async def game_handler(request):
    """Mój handler obsługujący połączenia z grą"""
    global current_turn
    
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    
    # Przypisuję symbol nowemu graczowi
    if len(players) == 0:
        symbol = 'X'
    elif len(players) == 1:
        symbol = 'O'
    else:
        # Jeśli jest już dwóch graczy, odrzucam kolejne połączenie
        await ws.send_json({"type": "error", "message": "Gra jest już pełna!"})
        await ws.close()
        return ws
        
    players[ws] = symbol
    print(f"Nowy gracz dołączył jako '{symbol}'.")
    
    # Informuję gracza, kim jest
    await ws.send_json({"type": "init", "symbol": symbol})
    # Rozsyłam aktualny stan gry do obu graczy
    await broadcast_state()
    
    try:
        # Nasłuchuję ruchów od graczy[cite: 1]
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                # Odbieram dane w formacie JSON[cite: 1]
                data = json.loads(msg.data)
                
                if data.get("type") == "move":
                    position = data.get("position")
                    
                    # Sprawdzam, czy to kolej tego gracza i czy pole jest puste
                    if players[ws] == current_turn and board[position] == ' ' and not check_winner():
                        # Aktualizuję planszę
                        board[position] = players[ws]
                        print(f"Gracz {players[ws]} zaznaczył pole {position}.")
                        
                        # Zmieniam kolejkę
                        current_turn = 'O' if current_turn == 'X' else 'X'
                        
                        # Rozsyłam aktualizację
                        await broadcast_state()
                    else:
                        await ws.send_json({"type": "error", "message": "Nieprawidłowy ruch lub to nie Twoja kolej!"})
                        
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print(f"Błąd gracza {symbol}: {ws.exception()}")
    finally:
        # Kiedy ktoś się rozłączy, usuwam go i resetuję grę dla pozostałych[cite: 1]
        print(f"Gracz '{symbol}' opuścił grę.")
        del players[ws]
        reset_game()
        await broadcast_state()
        
    return ws

app = web.Application()
app.router.add_get('/game', game_handler)

if __name__ == '__main__':
    print("Mój serwer kółko i krzyżyk działa na ws://localhost:8080/game")
    web.run_app(app, host='localhost', port=8080)