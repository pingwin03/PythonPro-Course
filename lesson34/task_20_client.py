import aiohttp
import asyncio
import json

my_symbol = None

def print_board(board):
    """Pomocnicza funkcja do ładnego rysowania planszy w konsoli"""
    print("\nObecna plansza:")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

async def receive_updates(ws):
    """Nasłuchuję zmian stanu gry w tle"""
    global my_symbol
    
    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            data = json.loads(msg.data)
            
            if data["type"] == "init":
                my_symbol = data["symbol"]
                print(f"--- Połączono z grą! Grasz jako: {my_symbol} ---")
                
            elif data["type"] == "update":
                print_board(data["board"])
                
                winner = data["winner"]
                if winner:
                    if winner == 'Tie':
                        print("Gra zakończona: REMIS!")
                    else:
                        print(f"Gra zakończona: ZWYCIĘŻA '{winner}'!")
                    # Gra się skończyła, wychodzę
                    break
                    
                if data["turn"] == my_symbol:
                    print(">>> TWÓJ RUCH! Wybierz pole (0-8): ")
                else:
                    print(f"Czekam na ruch przeciwnika ({data['turn']})...")
                    
            elif data["type"] == "error":
                print(f"[BŁĄD] {data['message']}")
                
async def game_client():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect('ws://localhost:8080/game') as ws:
            # Uruchamiam funkcję nasłuchującą w tle
            receive_task = asyncio.create_task(receive_updates(ws))
            
            # Główna pętla wprowadzania ruchów
            while not receive_task.done():
                try:
                    # Pobieram ruch od gracza z konsoli
                    move = await asyncio.to_thread(input, "")
                    
                    if receive_task.done():
                        break
                        
                    if move.isdigit() and 0 <= int(move) <= 8:
                        # Wysyłam ruch jako JSON[cite: 1]
                        await ws.send_json({
                            "type": "move",
                            "position": int(move)
                        })
                    else:
                        print("Podaj poprawną cyfrę od 0 do 8!")
                except Exception:
                    pass
                    
            print("Zamykam klienta gry.")

if __name__ == '__main__':
    print("Indeksy pól na planszy:")
    print(" 0 | 1 | 2 ")
    print(" 3 | 4 | 5 ")
    print(" 6 | 7 | 8 \n")
    asyncio.run(game_client())