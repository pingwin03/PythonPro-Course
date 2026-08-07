# Asynchroniczny ping: Napisz ping(host),
# śpiący losowy czas i zwracający potwierdzenie. Uruchom dla 5 hostów.

import asyncio
import random
import time

# Definiuję moją korutynę symulującą działanie komendy ping, przyjmującą adres hosta
async def ping(host):
    print(f"Wysyłam ping do: {host}...")
    
    # Losuję czas opóźnienia, np. od 0.5 do 2.5 sekund, używając funkcji z wbudowanego modułu random
    czas_odpowiedzi = random.uniform(0.5, 2.5)
    
    # Usypiam moją korutynę na wylosowany czas, symulując oczekiwanie na odpowiedź sieci
    await asyncio.sleep(czas_odpowiedzi)
    
    # Zwracam sformatowany tekst z potwierdzeniem i czasem odpowiedzi
    return f"Sukces! Host {host} odpowiedział w czasie {czas_odpowiedzi:.2f}s"

# Tworzę główną korutynę do zarządzania wykonaniem
async def main():
    # Zapisuję czas startu, aby sprawdzić współbieżność
    start = time.perf_counter()
    
    # Przygotowuję listę 5 przykładowych hostów
    hosty = [
        "192.168.1.1", 
        "127.0.0.1", 
        "google.com", 
        "github.com", 
        "python.org"
    ]
    
    # Używam asyncio.gather(), aby wysłać zapytania do wszystkich 5 hostów jednocześnie
    wyniki = await asyncio.gather(*(ping(host) for host in hosty))
    
    # Przechodzę przez listę zebranych wyników i wypisuję je na ekran
    print("\n--- Zestawienie wyników ---")
    for wynik in wyniki:
        print(wynik)
        
    # Wypisuję całkowity czas wykonania
    print(f"\nCałkowity czas pingowania 5 hostów: {time.perf_counter() - start:.2f}s")

# Uruchamiam główną pętlę zdarzeń
asyncio.run(main())