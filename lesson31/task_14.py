# Kolejka producent-konsument: Połącz zadania kolejką asyncio.
# Queue (1 ładuje liczby, 2 przetwarza je w locie).


import asyncio
import random

# Definiuję moją korutynę producenta, która przyjmuje obiekt kolejki jako argument
async def producent(kolejka):
    print("[Producent] Zaczynam generować liczby...")
    
    # Tworzę 5 przykładowych porcji danych
    for i in range(1, 6):
        # Symuluję czas potrzebny na wytworzenie danych (np. zapytanie do bazy)
        await asyncio.sleep(random.uniform(0.1, 0.5))
        
        liczba = random.randint(10, 99)
        print(f"[Producent] Wygenerowałem liczbę: {liczba}. Umieszczam ją w kolejce.")
        
        # Używam await kolejka.put(), aby asynchronicznie dodać element.
        # Jeśli kolejka miałaby ustawiony maksymalny rozmiar (maxsize) i byłaby pełna, 
        # ta linijka grzecznie poczekałaby na zwolnienie miejsca.
        await kolejka.put(liczba)
        
    # Kiedy skończę produkcję, wrzucam do kolejki wartość None (tzw. trujący pigułkę / poison pill),
    # aby dać znak konsumentowi, że to już koniec danych.
    print("[Producent] Skończyłem pracę. Wysyłam sygnał końca (None).")
    await kolejka.put(None)

# Tworzę moją korutynę konsumenta, która również korzysta z tej samej kolejki
async def konsument(kolejka):
    print("[Konsument] Zgłaszam gotowość do przetwarzania!")
    
    # Uruchamiam nieskończoną pętlę, która będzie nasłuchiwać nowych danych
    while True:
        # Używam await kolejka.get(), co usypia konsumenta do momentu, 
        # aż w kolejce pojawi się coś nowego
        element = await kolejka.get()
        
        # Sprawdzam, czy otrzymałem sygnał zakończenia od producenta
        if element is None:
            print("[Konsument] Otrzymałem sygnał końca. Zamykam warsztat.")
            # Oznaczam ten konkretny element (None) jako obsłużony
            kolejka.task_done()
            break
            
        print(f"[Konsument] Pobrałem z kolejki liczbę {element} i zaczynam przetwarzanie...")
        
        # Symuluję pracę nad pobranym elementem
        await asyncio.sleep(random.uniform(0.2, 0.8))
        print(f"[Konsument] Przetwarzanie liczby {element} zakończone sukcesem!")
        
        # Informuję kolejkę, że skończyłem pracę nad tym konkretnym zadaniem.
        # To bardzo ważny krok, jeśli później chcielibyśmy użyć kolejka.join()!
        kolejka.task_done()

# Główna korutyna sterująca
async def main():
    # Inicjalizuję moją asynchroniczną kolejkę
    wspolna_kolejka = asyncio.Queue()
    
    # Używam asyncio.gather(), aby wystartować producenta i konsumenta w tym samym czasie.
    # Przekazuję im ten sam obiekt kolejki, aby mogły się ze sobą komunikować.
    await asyncio.gather(
        producent(wspolna_kolejka),
        konsument(wspolna_kolejka)
    )
    
    print("\nWszystkie zadania w systemie producent-konsument zostały pomyślnie zakończone.")

# Uruchamiam program
if __name__ == "__main__":
    asyncio.run(main())