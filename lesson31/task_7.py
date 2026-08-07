# Wiele miast: Wywołaj pobierz_pogode współbieżnie dla 3 różnych miast.

import asyncio
import time

# Wykorzystuję moją korutynę z poprzedniego zadania
async def pobierz_pogode(miasto):
    print(f"Rozpoczynam pobieranie danych pogodowych dla miasta: {miasto}...")
    
    # Symuluję opóźnienie sieciowe
    await asyncio.sleep(1.5)
    
    # Zwracam słownik z danymi
    return {
        "miasto": miasto,
        "temperatura": 22,
        "stan": "Słonecznie",
        "wiatr": "12 km/h"
    }

# Tworzę główną korutynę zarządzającą
async def main():
    # Zapisuję czas startu, aby udowodnić współbieżne działanie
    start = time.perf_counter()
    
    # Definiuję listę moich miast
    miasta = ["Warszawa", "Kraków", "Gdańsk"]
    
    # Używam asyncio.gather, aby wywołać moją korutynę dla każdego miasta z listy w tym samym czasie
    wyniki = await asyncio.gather(*(pobierz_pogode(miasto) for miasto in miasta))
    
    # Przechodzę przez listę wyników i wypisuję je na ekran
    for wynik in wyniki:
        print(f"Dane: {wynik}")
        
    # Wypisuję całkowity czas wykonania
    print(f"Całkowity czas wykonania dla 3 miast: {time.perf_counter() - start:.2f}s")

# Uruchamiam główną pętlę zdarzeń
asyncio.run(main())