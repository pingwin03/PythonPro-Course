# Sumowanie wyników zadań: Stwórz 10 zadań losujących wynik po 2-5s. 
# Użyj gather i wysumuj rezultaty.

import asyncio
import random
import time

# Definiuję moją korutynę, która przyjmuje identyfikator zadania w celach informacyjnych
async def losuj_wynik(id_zadania):
    # Losuję czas uśpienia z przedziału od 2 do 5 sekund
    czas_oczekiwania = random.uniform(2, 5)
    print(f"[Zadanie {id_zadania}] Zaczynam pracę. Będę spać przez {czas_oczekiwania:.2f}s...")
    
    # Oddaję kontrolę do pętli zdarzeń na wylosowany czas
    await asyncio.sleep(czas_oczekiwania)
    
    # Losuję ostateczny wynik, np. liczbę całkowitą od 1 do 100
    wylosowana_wartosc = random.randint(1, 100)
    print(f"[Zadanie {id_zadania}] Pobudka! Zwracam wynik: {wylosowana_wartosc}")
    
    # Zwracam wylosowaną wartość
    return wylosowana_wartosc

# Tworzę moją główną korutynę zarządzającą
async def main():
    print("Uruchamiam 10 zadań losujących...\n")
    start = time.perf_counter()
    
    # Buduję listę 10 zadań, używając pętli i przekazując numer zadania od 1 do 10
    zadania = [losuj_wynik(i) for i in range(1, 11)]
    
    # Zbieram wszystkie zwrócone wyniki współbieżnie za pomocą asyncio.gather
    # Wyniki zostaną zwrócone w formie listy w takiej samej kolejności, w jakiej stworzyłem zadania
    zebrane_wyniki = await asyncio.gather(*zadania)
    
    # Sumuję otrzymane rezultaty przy użyciu wbudowanej funkcji sum()
    suma_calkowita = sum(zebrane_wyniki)
    
    print("\n--- Podsumowanie ---")
    print(f"Lista zebranych wyników: {zebrane_wyniki}")
    print(f"Całkowita suma wyników: {suma_calkowita}")
    
    # Wypisuję całkowity czas wykonania, aby pokazać wydajność współbieżności
    czas_trwania = time.perf_counter() - start
    print(f"Cały proces zajął tylko: {czas_trwania:.2f}s")

# Uruchamiam główną pętlę zdarzeń
if __name__ == "__main__":
    asyncio.run(main())
