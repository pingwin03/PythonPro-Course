# Współbieżne odliczanie: Zbuduj 3 korutyny zliczające czas w dół 
# i wypisujące go, każda pracująca niezależnie, z różnym czasem początkowym.


import asyncio

# Definiuję moją korutynę, która przyjmuje nazwę (identyfikator) oraz startowy czas odliczania
async def odliczanie(nazwa, czas_poczatkowy):
    print(f"[{nazwa}] Rozpoczynam odliczanie od {czas_poczatkowy}...")
    
    # Używam pętli, aby schodzić z czasem w dół aż do 1
    for i in range(czas_poczatkowy, 0, -1):
        print(f"[{nazwa}] Pozostało: {i} sekundy...")
        # Wprowadzam asynchroniczną pauzę na 1 sekundę. W tym momencie Event Loop 
        # przełącza się na inne działające odliczania!
        await asyncio.sleep(1)
        
    print(f"[{nazwa}] Koniec odliczania!")

# Tworzę główną korutynę zarządzającą
async def main():
    print("Startuję wszystkie odliczania współbieżnie...\n")
    
    # Używam asyncio.gather(), aby zlecić pętli zdarzeń wykonanie trzech korutyn jednocześnie
    # Każdej z nich nadaję unikalną nazwę i różny czas początkowy
    await asyncio.gather(
        odliczanie("Licznik A", 3),
        odliczanie("Licznik B", 5),
        odliczanie("Licznik C", 2)
    )
    
    print("\nWszystkie liczniki zakończyły swoją pracę.")

# Uruchamiam główną pętlę zdarzeń
if __name__ == "__main__":
    asyncio.run(main())