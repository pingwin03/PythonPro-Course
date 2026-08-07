# Korutyna zwracająca wartość: Napisz oblicz_potege(liczba, potega) (2s opóźnienia) i zwróć wynik.


import asyncio

# Definiuję moją korutynę, która przyjmuje dwie wartości: podstawę (liczba) i wykładnik (potega)
async def oblicz_potege(liczba, potega):
    print(f"Rozpoczynam obliczanie {liczba} do potęgi {potega}...")
    
    # Wprowadzam wymagane opóźnienie, usypiając moją korutynę na 2 sekundy
    await asyncio.sleep(2)
    
    # Obliczam i od razu zwracam wynik
    return liczba ** potega

# Tworzę główną funkcję sterującą
async def main():
    # Używam await, aby poczekać na zakończenie obliczeń, a zwróconą wartość przypisuję do zmiennej
    wynik = await oblicz_potege(3, 4)
    
    # Wypisuję otrzymany wynik na ekran
    print(f"Obliczony wynik to: {wynik}")

# Uruchamiam pętlę zdarzeń za pomocą asyncio.run()
asyncio.run(main())