# Generator asynchroniczny: Użyj pętli async for wraz
# z słowem kluczowym yield asynchronicznie produkującym nowe dane.


import asyncio
import random

# Definiuję mój asynchroniczny generator. Zauważ, że używam 'async def',
# ale zamiast 'return' na końcu (co zwróciłoby wartość i zakończyło funkcję),
# używam słowa kluczowego 'yield' wewnątrz pętli.
async def strumien_alertow_bezpieczenstwa():
    print("[Strumień] Nawiązuję połączenie z zewnętrznym źródłem (np. CERT Polska)...")
    
    # Tworzę przykładową bazę potencjalnych zdarzeń
    typy_zdarzen = [
        "Wykryto próbę logowania z podejrzanego IP",
        "Aktualizacja sygnatur dla złośliwego oprogramowania",
        "Nietypowy ruch na zaporze sieciowej",
        "Powiadomienie o nowej kampanii phishingowej",
        "Blokada skanowania portów zidentyfikowana"
    ]
    
    # Symuluję ciągły nasłuch - w tym przykładzie wygeneruję 5 powiadomień
    for numer_alertu in range(1, 6):
        # Asynchronicznie czekam, symulując losowy czas pomiędzy
        # pojawieniem się kolejnych incydentów w sieci.
        await asyncio.sleep(random.uniform(0.5, 2.0))
        
        tresc_alertu = random.choice(typy_zdarzen)
        raport = f"INC-2026-{numer_alertu:04d}: {tresc_alertu}"
        
        # Tutaj dzieje się asynchroniczna magia!
        # Oddaję wygenerowany raport do głównej pętli (konsumenta), ale
        # nie kończę działania samej funkcji. Moja korutyna zostaje tu 
        # "zamrożona", dopóki konsument nie poprosi o następny element.
        yield raport
        
    print("[Strumień] Transmisja z tego źródła została zakończona.")

# Główna korutyna zarządzająca programem
async def main():
    print("Główny program: Uruchamiam agregator wiadomości.\n")
    
    # Aby odczytać dane z asynchronicznego generatora, muszę użyć specjalnej
    # konstrukcji 'async for'. Standardowe 'for' spowodowałoby błąd.
    # Pętla ta pozwala na wykonywanie asynchronicznych uśpień w tle,
    # w oczekiwaniu na kolejne wywołanie 'yield'.
    async for alert in strumien_alertow_bezpieczenstwa():
        # Kiedy generator zrobi 'yield', kod natychmiast trafia tutaj
        print(f"[Agregator] Przechwycono nowe zdarzenie w czasie rzeczywistym -> {alert}")
        
        # Symuluję krótkie, bieżące przetwarzanie otrzymanego alertu 
        # (np. formatowanie i zapis do bazy danych agregatora)
        await asyncio.sleep(0.1)
        
    print("\nGłówny program: Agregator przetworzył na bieżąco wszystkie dostępne zdarzenia.")

# Uruchamiam program
if __name__ == "__main__":
    asyncio.run(main())