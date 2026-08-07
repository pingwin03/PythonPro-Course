# Asynchroniczny licznik: Napisz korutynę licznik(n), która co sekundę wypisuje liczby od 1 do n używając await asyncio.sleep(1)



import asyncio

# Definiuję moją korutynę, która przyjmuje parametr 'n'
async def licznik(n):
    # Używam pętli for, aby przejść przez liczby od 1 do n włącznie
    for i in range(1, n + 1):
        # Wypisuję na ekran obecną wartość
        print(i)
        # Usypiam moją korutynę na 1 sekundę, grzecznie oddając kontrolę do pętli zdarzeń
        await asyncio.sleep(1)

# Uruchamiam główną pętlę zdarzeń i wywołuję mój licznik, na przykład z wartością 5
asyncio.run(licznik(5))