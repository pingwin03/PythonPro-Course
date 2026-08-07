# Asynchroniczny zapis do pliku: Użyj asyncio.Lock i biblioteki aiofiles, 
# aby 5 zadań bezpiecznie pisało logi do jednego pliku.


# pip install aiofiles

import asyncio
import aiofiles
import time
import random

# Definiuję moją korutynę, która będzie zapisywać logi do pliku
async def zapisz_log(id_zadania, blokada, nazwa_pliku):
    # Symuluję jakąś pracę przed zapisem logu, śpiąc przez losowy czas
    await asyncio.sleep(random.uniform(0.1, 1.0))
    
    print(f"[Zadanie {id_zadania}] Zgłaszam chęć zapisu i czekam na zwolnienie blokady...")
    
    # Używam menedżera kontekstu "async with" dla blokady. 
    # Jeśli inne zadanie aktualnie zapisuje plik, moja korutyna w tym miejscu poczeka.
    async with blokada:
        print(f"[Zadanie {id_zadania}] Dostałem klucz! Zapisuję log...")
        
        # Otwieram plik asynchronicznie w trybie dopisywania ('a' - append)
        async with aiofiles.open(nazwa_pliku, mode='a', encoding='utf-8') as plik:
            # Przygotowuję format wiadomości z dokładnym czasem
            aktualny_czas = time.strftime('%H:%M:%S')
            wiadomosc = f"Log z Zadania {id_zadania} | Wygenerowano o: {aktualny_czas}\n"
            
            # Asynchronicznie zapisuję tekst do pliku
            await plik.write(wiadomosc)
            
            # Symuluję bardzo wolny dysk, aby pokazać, że inne zadania faktycznie czekają
            await asyncio.sleep(0.5) 
            
        print(f"[Zadanie {id_zadania}] Zapis zakończony. Oddaję klucz i zwalniam blokadę.")

# Tworzę moją główną korutynę zarządzającą
async def main():
    plik_logow = "system_log.txt"
    
    # Inicjalizuję moją blokadę. Tworzę tylko jeden taki obiekt i przekazuję go do wszystkich zadań.
    wspolna_blokada = asyncio.Lock()
    
    # Tworzę listę 5 zadań
    zadania = [zapisz_log(i, wspolna_blokada, plik_logow) for i in range(1, 6)]
    
    print("Uruchamiam 5 zadań próbujących zapisać dane do jednego pliku...\n")
    
    # Uruchamiam wszystkie zadania współbieżnie
    await asyncio.gather(*zadania)
    
    print(f"\nWszystkie logi zostały bezpiecznie zapisane do pliku: {plik_logow}")

# Uruchamiam główną pętlę zdarzeń
if __name__ == "__main__":
    asyncio.run(main())