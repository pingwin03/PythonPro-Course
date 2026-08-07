# Prosty serwer echa: Napisz serwer TCP na localhost:8888 za pomocą asyncio.start_server().


import asyncio

# Definiuję moją korutynę, która zajmie się obsługą pojedynczego połączenia klienta.
# Zawsze otrzymuje ona dwa obiekty: reader (do czytania danych) i writer (do wysyłania danych).
async def obsluz_klienta(reader, writer):
    # Wyciągam informacje o adresie IP i porcie podłączonego klienta
    adres = writer.get_extra_info('peername')
    print(f"[Serwer] Nawiązałem połączenie z {adres}")
    
    # Czekam asynchronicznie na dane od klienta. 
    # Zakładam tutaj odczyt maksymalnie 100 bajtów.
    dane = await reader.read(100)
    
    # Otrzymane dane są w formacie bajtów (bytes), więc dekoduję je do zwykłego tekstu
    wiadomosc = dane.decode()
    print(f"[Serwer] Otrzymałem wiadomość: {wiadomosc!r} od {adres}")
    
    # Wysyłam dokładnie te same bajty z powrotem do klienta (funkcja echa)
    print(f"[Serwer] Odsyłam echo: {wiadomosc!r}")
    writer.write(dane)
    
    # Używam await writer.drain(), aby upewnić się, że dane zostały fizycznie 
    # wypchnięte z bufora sieciowego do klienta przed zamknięciem połączenia
    await writer.drain()
    
    # Zamykam połączenie z mojej strony
    print(f"[Serwer] Zamykam połączenie z {adres}\n")
    writer.close()
    
    # Grzecznie czekam, aż system operacyjny potwierdzi całkowite zamknięcie gniazda
    await writer.wait_closed()

# Tworzę główną korutynę zarządzającą moim serwerem
async def main():
    print("[Serwer] Uruchamiam asynchroniczny serwer TCP na localhost:8888...")
    
    # Tworzę instancję serwera. Przekazuję funkcję obsługującą, adres (localhost) oraz port (8888)
    serwer = await asyncio.start_server(
        obsluz_klienta, '127.0.0.1', 8888)

    # Używam menedżera kontekstu "async with", aby mieć pewność, że po zatrzymaniu 
    # programu zasoby serwera zostaną prawidłowo zwolnione
    async with serwer:
        # Odpalam serwer w nieskończonej pętli, aby stale nasłuchiwał nowych połączeń
        await serwer.serve_forever()

# Uruchamiam główną pętlę zdarzeń
if __name__ == "__main__":
    # Dodaję prostą obsługę bloku try-except, aby móc ładnie zatrzymać serwer
    # używając skrótu klawiszowego Ctrl+C w terminalu
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[Serwer] Działanie serwera zostało zatrzymane.")