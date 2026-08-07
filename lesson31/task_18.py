# Anulowanie zadania: Uruchom task z pętlą while(True), w głównym programie wymuś po 5 sekundach 
# .cancel() i przechwyć ten błąd asynchronicznie w samym tasku.


import asyncio

# Definiuję moją korutynę, która będzie działać w nieskończonej pętli
async def ciagly_nasluch():
    print("[Zadanie] Uruchamiam nieprzerwany monitoring strumienia danych...")
    
    try:
        # Moja nieskończona pętla
        numer_skanu = 1
        while True:
            print(f"[Zadanie] Przeprowadzam skanowanie nr {numer_skanu}...")
            numer_skanu += 1
            
            # Aby pętla nie zablokowała głównego wątku, muszę oddać sterowanie 
            # za pomocą asynchronicznego uśpienia. To właśnie tutaj wstrzyknięty 
            # zostanie wyjątek CancelledError, gdy wywołam .cancel()!
            await asyncio.sleep(1)
            
    except asyncio.CancelledError:
        # Asynchronicznie przechwytuję wymuszone zatrzymanie
        print("\n[Zadanie] UWAGA: Otrzymałem sygnał anulowania (CancelledError)!")
        print("[Zadanie] Rozpoczynam procedurę bezpiecznego zamykania...")
        
        # Tutaj mogę wykonać ostatnie asynchroniczne operacje czyszczące
        await asyncio.sleep(0.5) 
        print("[Zadanie] Sprzątanie zakończone. Wyłączam się.")
        
        # Zgodnie z dobrymi praktykami, po obsłużeniu sprzątania należy 
        # rzucić ten wyjątek dalej, aby pętla zdarzeń wiedziała, że zadanie 
        # faktycznie zostało anulowane, a nie zakończyło się naturalnie.
        raise

# Główna korutyna zarządzająca programem
async def main():
    print("Główny program: Start systemu.")
    
    # Uruchamiam moje zadanie w tle przy użyciu create_task
    zadanie_w_tle = asyncio.create_task(ciagly_nasluch())
    
    print("Główny program: Zadanie w tle uruchomione. Odmierzam 5 sekund...\n")
    
    # Pozwalam systemowi działać równo przez 5 sekund
    await asyncio.sleep(5)
    
    print("\nGłówny program: Minęło 5 sekund. Wymuszam anulowanie zadania (.cancel()).")
    # Wysyłam sygnał zatrzymania do mojego zadania
    zadanie_w_tle.cancel()
    
    # Czekam na ostateczne rozwiązanie zadania. Ponieważ rzuci ono błędem
    # CancelledError na samym końcu, muszę go złapać tutaj, by program
    # nie zakończył się nieestetycznym zrzutem błędu w konsoli (traceback).
    try:
        await zadanie_w_tle
    except asyncio.CancelledError:
        print("Główny program: Potwierdzam, zadanie w tle zostało w pełni i bezpiecznie anulowane.")

# Uruchamiam program
if __name__ == "__main__":
    asyncio.run(main())