# Kto pierwszy, ten lepszy: Użyj asyncio.wait() na 5 zadaniach
# z parametrem FIRST_COMPLETED. Wypisz wynik tego, które skończyło jako pierwsze.


import asyncio
import random

# Definiuję moją korutynę reprezentującą zawodnika w wyścigu
async def wyscig(id_zawodnika):
    # Losuję czas, w jakim zawodnik ukończy zadanie (od 1 do 5 sekund)
    czas_biegu = random.uniform(1, 5)
    print(f"[Zawodnik {id_zawodnika}] Rozpoczynam bieg! Potrzebuję {czas_biegu:.2f}s...")
    
    # Symuluję pracę poprzez asynchroniczne uśpienie
    await asyncio.sleep(czas_biegu)
    
    # Zwracam string z informacją o zawodniku
    return f"Zawodnik {id_zawodnika} (czas: {czas_biegu:.2f}s)"

# Tworzę główną korutynę zarządzającą
async def main():
    print("Rozpoczynamy wyścig 5 zawodników...\n")
    
    # Do asyncio.wait() najlepiej przekazywać obiekty typu Task, 
    # dlatego owijam moje korutyny za pomocą asyncio.create_task()
    zadania = [asyncio.create_task(wyscig(i)) for i in range(1, 6)]
    
    # Przekazuję listę zadań do asyncio.wait() i ustawiam warunek zakończenia 
    # na FIRST_COMPLETED, aby program poszedł dalej po pierwszym sukcesie
    zrobione, w_toku = await asyncio.wait(zadania, return_when=asyncio.FIRST_COMPLETED)
    
    # Zmienna 'zrobione' jest zbiorem (set), więc wydobywam z niej 
    # zakończone zadanie za pomocą metody pop()
    zwycieskie_zadanie = zrobione.pop()
    
    # Używam metody .result() na obiekcie Task, aby wyciągnąć wartość zwróconą przez korutynę
    wynik = zwycieskie_zadanie.result()
    
    print(f"\n--- WYNIKI ---")
    print(f"Mamy zwycięzcę! Został nim: {wynik}")
    print(f"Liczba zadań wciąż trwających (pending): {len(w_toku)}")
    
    # Dobrą praktyką jest anulowanie zadań, które jeszcze trwają i nie są nam już potrzebne
    for zadanie in w_toku:
        zadanie.cancel()

# Uruchamiam główną pętlę zdarzeń
if __name__ == "__main__":
    asyncio.run(main())