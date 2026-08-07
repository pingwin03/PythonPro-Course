# Dwa zadania po kolei: Stwórz zadanie1 (śpi 2s) i zadanie2 (śpi 1s). Wykonaj je sekwencyjnie.



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

# Tworzę główną korutynę do zarządzania wykonaniem
async def main():
    # Zapisuję czas startu, aby sprawdzić, ile potrwa całość
    start = time.perf_counter()
    
    # Wywołuję zadanie 1 i grzecznie czekam na jego zakończenie
    await zadanie1()
    
    # Dopiero gdy zadanie 1 się skończy, wywołuję i czekam na zadanie 2
    await zadanie2()
    
    # Wypisuję całkowity czas wykonania
    print(f"Całkowity czas wykonania: {time.perf_counter() - start:.2f}s")

# Uruchamiam główną pętlę zdarzeń
asyncio.run(main())