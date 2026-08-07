# Timeout dla zadania: Uśpij zadanie na losowy czas (1-5s). 
# Zabezpiecz go używając wait_for z timeout=3, obsłuż poprawnie TimeoutError.


import asyncio
import random

# Definiuję moją korutynę, która symuluje nieprzewidywalną operację (np. wolne API)
async def powolna_operacja_sieciowa():
    # Losuję czas trwania operacji od 1 do 5 sekund
    czas_pracy = random.uniform(1.0, 5.0)
    print(f"[Zadanie] Rozpoczynam łączenie z serwerem. Potrzebuję na to {czas_pracy:.2f} sekund...")
    
    try:
        # Symuluję asynchroniczne oczekiwanie (pracę wejścia/wyjścia)
        await asyncio.sleep(czas_pracy)
        
        # Ten kod wykona się tylko, jeśli zadanie zdąży przed timeoutem
        print(f"[Zadanie] Operacja zakończona sukcesem w czasie {czas_pracy:.2f}s!")
        return "Zwracam ważne dane z serwera"
        
    except asyncio.CancelledError:
        # Pamiętasz zadanie 18? wait_for wysyła CancelledError, gdy czas minie!
        print("[Zadanie] Auć! Dostałem sygnał anulowania (czas minął) w trakcie pracy.")
        # Rzucam wyjątek dalej, aby wait_for poprawnie wygenerowało TimeoutError
        raise

# Główna korutyna zarządzająca
async def main():
    limit_czasu = 3.0
    print(f"Główny program: Zlecam zadanie. Ustawiam nieprzekraczalny limit czasu na {limit_czasu}s.\n")
    
    try:
        # Używam asyncio.wait_for, przekazując wywołanie korutyny oraz mój limit czasowy
        wynik = await asyncio.wait_for(powolna_operacja_sieciowa(), timeout=limit_czasu)
        
        # Jeśli się uda, po prostu odbieram wynik
        print(f"\nGłówny program: Sukces! Odebrałem wynik: '{wynik}'")
        
    except asyncio.TimeoutError:
        # Ten blok przechwytuje sytuację, w której czas oczekiwania zostanie przekroczony
        print("\nGłówny program: BŁĄD TIMEOUTU! Zadanie trwało zbyt długo i zostało awaryjnie przerwane.")
        print("Główny program: Wdrażam plan B (np. załadowanie domyślnych danych z pamięci cache).")

# Uruchamiam program
if __name__ == "__main__":
    asyncio.run(main())