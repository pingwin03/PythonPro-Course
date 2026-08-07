# Dwa zadania współbieżnie: Zmodyfikuj zadanie 3 – użyj asyncio.gather(). Zmierz i porównaj czas.


import asyncio
import time

# Definiuję moje pierwsze zadanie, które będzie spać przez 2 sekundy
async def zadanie1():
    print("Rozpoczynam zadanie 1 (czas trwania: 2s)...")
    await asyncio.sleep(2)
    print("Zadanie 1 zakończone.")

# Definiuję moje drugie zadanie, które będzie spać przez 1 sekundę
async def zadanie2():
    print("Rozpoczynam zadanie 2 (czas trwania: 1s)...")
    await asyncio.sleep(1)
    print("Zadanie 2 zakończone.")

# Tworzę główną korutynę
async def main():
    # Zapisuję czas startu, abym mógł zmierzyć i porównać, ile potrwa całość
    start = time.perf_counter()
    
    # Używam asyncio.gather(), aby zlecić wykonanie obu moich zadań współbieżnie
    await asyncio.gather(zadanie1(), zadanie2())
    
    # Wypisuję całkowity czas wykonania do porównania z poprzednim wynikiem
    print(f"Całkowity czas wykonania współbieżnego: {time.perf_counter() - start:.2f}s")

# Uruchamiam główną pętlę zdarzeń
asyncio.run(main())