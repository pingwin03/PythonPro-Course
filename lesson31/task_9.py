# Pobieranie statusów HTTP: Używając httpx zbadaj kody statusów dla listy podanych URLi.

# pip install httpx





import asyncio
import httpx

# Definiuję moją korutynę, która sprawdzi status pojedynczego adresu URL
# Jako argumenty przyjmuję sam adres oraz instancję asynchronicznego klienta
async def sprawdz_status(url: str, client: httpx.AsyncClient):
    print(f"Wysyłam zapytanie do: {url}...")
    
    try:
        # Używam await, aby grzecznie poczekać na odpowiedź, pozwalając innym URL-om ładować się w tle
        response = await client.get(url)
        # Zwracam adres wraz z otrzymanym kodem statusu (np. 200, 404)
        return f"{url} -> Kod statusu: {response.status_code}"
    except httpx.RequestError as e:
        # Przechwytuję ewentualne błędy połączenia (np. błędny adres, brak sieci)
        return f"{url} -> Błąd połączenia: {e}"

# Tworzę główną korutynę zarządzającą
async def main():
    # Przygotowuję listę przykładowych adresów URL do zbadania
    urle = [
        "https://www.python.org",
        "https://www.github.com",
        "https://httpbin.org/status/404", # Ten URL celowo zwróci status 404 Not Found
        "https://httpbin.org/status/500"  # Ten URL celowo zwróci status 500 Internal Server Error
    ]
    
    # Otwieram sesję asynchronicznego klienta używając menedżera kontekstu (async with)
    # Zgodnie z zaleceniami ustawiam globalny timeout na 10 sekund
    async with httpx.AsyncClient(timeout=10.0) as client:
        
        # Tworzę listę zadań do wykonania dla każdego URL-a
        zadania = [sprawdz_status(url, client) for url in urle]
        
        # Używam asyncio.gather(), aby wysłać wszystkie zapytania współbieżnie
        wyniki = await asyncio.gather(*zadania)
        
        # Przechodzę przez zebrane wyniki i wypisuję je na ekran
        print("\n--- Podsumowanie statusów HTTP ---")
        for wynik in wyniki:
            print(wynik)

# Uruchamiam program
if __name__ == "__main__":
    asyncio.run(main())