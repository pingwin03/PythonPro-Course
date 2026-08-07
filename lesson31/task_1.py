# Pierwsza korutyna: Napisz korutynę, która po uruchomieniu wypisze “Gotowy do nauki!”. Uruchom ją.




import asyncio

# Definiuję moją pierwszą korutynę za pomocą 'async def'
async def pierwsza_korutyna():
    # Wypisuję na ekranie wymagany tekst
    print("Gotowy do nauki!")

# Uruchamiam moją korutynę używając asyncio.run(), co odpala pętlę zdarzeń
asyncio.run(pierwsza_korutyna())