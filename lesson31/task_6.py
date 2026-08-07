# Symulacja pobierania danych: Napisz korutynę pobierz_pogode(miasto)
# z 1.5s uśpieniem i słownikiem zwrotnym.


import asyncio

# Definiuję moją korutynę, która jako argument przyjmuje nazwę miasta
async def pobierz_pogode(miasto):
    print(f"Rozpoczynam pobieranie danych pogodowych dla miasta: {miasto}...")
    
    # Symuluję opóźnienie sieciowe (oczekiwanie na odpowiedź serwera), usypiając moją korutynę na 1.5 sekundy
    await asyncio.sleep(1.5)
    
    # Tworzę i zwracam słownik z fikcyjnymi, symulowanymi danymi pogodowymi
    return {
        "miasto": miasto,
        "temperatura": 22,
        "stan": "Słonecznie",
        "wiatr": "12 km/h"
    }

# Tworzę główną korutynę, aby przetestować moje rozwiązanie
async def main():
    # Używam await, aby grzecznie poczekać na pobranie danych z mojej symulacji
    wynik = await pobierz_pogode("Warszawa")
    
    # Wypisuję zwrócony słownik na ekran
    print(f"Pobrane dane: {wynik}")

# Uruchamiam główną pętlę zdarzeń
asyncio.run(main())