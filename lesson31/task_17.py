# Łańcuch zależności: Napisz kaskadę: pobranie User ID -> pobranie wpisów -> 
# pobranie komentarzy. Używaj gather dla list na końcu łańcucha.


import asyncio
import random

# Krok 1 w kaskadzie: Korutyna pobierająca ID użytkownika (np. identyfikator źródła)
async def pobierz_user_id(nazwa_konta):
    print(f"[Krok 1] Szukam ID dla konta: {nazwa_konta}...")
    await asyncio.sleep(random.uniform(0.5, 1.0)) # Symuluję zapytanie do bazy/API
    
    # Zwracam przykładowe ID
    znalezione_id = 998
    print(f"[Krok 1] Znalazłem! {nazwa_konta} ma User ID = {znalezione_id}")
    return znalezione_id

# Krok 2 w kaskadzie: Korutyna pobierająca listę wpisów dla konkretnego User ID
async def pobierz_wpisy(user_id):
    print(f"[Krok 2] Pobieram najnowsze wpisy dla User ID: {user_id}...")
    await asyncio.sleep(random.uniform(0.5, 1.5))
    
    # Zwracam listę słowników symulujących wpisy/alerty bezpieczeństwa
    wpisy = [
        {"post_id": 101, "tytul": "Nowa kampania phishingowa na bramki płatności"},
        {"post_id": 102, "tytul": "Aktualizacja systemów zaporowych (CSIRT GOV)"},
        {"post_id": 103, "tytul": "Raport z incydentu naruszenia danych"}
    ]
    print(f"[Krok 2] Sukces. Pobrałem {len(wpisy)} wpisy.")
    return wpisy

# Krok 3 w kaskadzie: Korutyna pobierająca komentarze/statusy dla pojedynczego wpisu
async def pobierz_komentarze(post_id):
    print(f"  -> [Krok 3] Żądam pobrania komentarzy dla post_id={post_id}...")
    await asyncio.sleep(random.uniform(1.0, 2.0))
    
    # Zwracam przykładową listę komentarzy zaktualizowaną przez analityków
    komentarze = [
        f"Zgłoszenie {post_id} przekazane do weryfikacji.",
        f"Aktualizacja statusu dla {post_id}: w toku."
    ]
    return komentarze

# Główna korutyna sterująca przepływem kaskady
async def main():
    print("Rozpoczynam pobieranie łańcucha zależności...\n")
    
    # Kaskada sekwencyjna (jedno zależy od drugiego)
    # Muszę użyć standardowego await, bo bez User ID nie ruszę dalej
    moje_user_id = await pobierz_user_id("CERT_Polska_Alerts")
    
    # Mając User ID, pobieram wpisy
    lista_wpisow = await pobierz_wpisy(moje_user_id)
    
    print("\nPrzechodzę do pobierania komentarzy dla wszystkich wpisów JEDNOCZEŚNIE...")
    
    # Tutaj dzieje się magia! Ponieważ mam już listę wpisów, komentarze dla każdego 
    # z nich mogę pobrać całkowicie niezależnie i współbieżnie.
    
    # Generuję listę zadań do wykonania na samym końcu łańcucha
    zadania_komentarzy = [pobierz_komentarze(wpis["post_id"]) for wpis in lista_wpisow]
    
    # Używam asyncio.gather, aby wysłać wszystkie zapytania o komentarze równolegle
    zebrane_komentarze = await asyncio.gather(*zadania_komentarzy)
    
    print("\n--- Podsumowanie pobierania ---")
    # Wyświetlam połączone dane (używam funkcji zip, aby połączyć wpis z jego komentarzami)
    for wpis, komentarze in zip(lista_wpisow, zebrane_komentarze):
        print(f"\nWpis: {wpis['tytul']}")
        for kom in komentarze:
            print(f"  - {kom}")

# Uruchamiam program
if __name__ == "__main__":
    asyncio.run(main())