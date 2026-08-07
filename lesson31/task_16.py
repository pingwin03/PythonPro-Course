# Integracja synchroniczna: Napisz program odczytujący 100 małych plików z dysku asynchronicznie, 
# wykorzystując systemowe IO przez asyncio.to_thread.



import asyncio
import os
import time

# Pomocnicza funkcja synchroniczna, która tworzy 100 małych plików testowych na dysku.
def przygotuj_pliki_testowe():
    os.makedirs("testowe_pliki", exist_ok=True)
    for i in range(1, 101):
        with open(f"testowe_pliki/plik_{i}.txt", "w", encoding="utf-8") as f:
            f.write(f"To jest tajna zawartość pliku numer {i}")

# Moja tradycyjna, synchroniczna funkcja blokująca, która po prostu czyta plik
def synchroniczny_odczyt(sciezka_do_pliku):
    # W celach demonstracyjnych nie dodaję tu time.sleep, bo sam odczyt 
    # z dysku jest dla Pythona operacją wejścia/wyjścia (I/O).
    with open(sciezka_do_pliku, "r", encoding="utf-8") as plik:
        return plik.read()

# Definiuję moją korutynę, która asynchronicznie obsłuży synchroniczny odczyt
async def odczytaj_asynchronicznie(sciezka, id_pliku):
    # Używam asyncio.to_thread, podając najpierw funkcję, którą chcę wywołać, 
    # a następnie jej argumenty. W tym czasie Event Loop działa dalej!
    zawartosc = await asyncio.to_thread(synchroniczny_odczyt, sciezka)
    
    # Zwracam informację o udanym odczycie
    return f"[Plik {id_pliku}] Odczytano {len(zawartosc)} znaków."

# Tworzę główną korutynę zarządzającą
async def main():
    print("Trwa przygotowywanie 100 plików testowych...")
    przygotuj_pliki_testowe()
    print("Pliki gotowe. Rozpoczynam współbieżny odczyt!\n")
    
    start_czas = time.perf_counter()
    
    # Buduję listę ścieżek do moich 100 plików
    sciezki = [f"testowe_pliki/plik_{i}.txt" for i in range(1, 101)]
    
    # Tworzę listę 100 zadań
    zadania = [odczytaj_asynchronicznie(sciezka, i) for i, sciezka in enumerate(sciezki, 1)]
    
    # Wykorzystuję znane nam już asyncio.gather, by wywołać to wszystko naraz
    wyniki = await asyncio.gather(*zadania)
    
    czas_trwania = time.perf_counter() - start_czas
    
    print("--- Podsumowanie ---")
    print(f"Sukces! Odczytałem {len(wyniki)} plików używając asyncio.to_thread.")
    # Wypisuję 3 pierwsze wyniki dla pewności, że zadziałało
    print(f"Próbka wyników: {wyniki[:3]} ...")
    print(f"Całkowity czas odczytu systemowego I/O: {czas_trwania:.4f}s")

# Uruchamiam program
if __name__ == "__main__":
    asyncio.run(main())