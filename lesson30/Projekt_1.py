# Projekt 1: Wielowątkowy Downloader Plików z Licznikiem Postępu
# Napisz skrypt, który pobiera zawartość z zestawu testowych adresów URL w sposób współbieżny. System musi zliczać globalną liczbę pobranych bajtów i bezpiecznie aktualizować licznik.

# Konfiguracja infrastruktury bazowej: 
#     Krok 1. Zdefiniuj listę 5-10 testowych adresów URL (można wykorzystać zasób 
#     [https://httpbin.org/bytes/1024](https://httpbin.org/bytes/1024) generujący losowe bajty o określonej długości). 
#     Przygotuj zmienną globalną TOTAL_BYTES_DOWNLOADED = 0 oraz obiekt typu Lock.

# Implementacja funkcji pobierającej: 
#     Krok 2. Stwórz funkcję wykonującą pojedyncze zapytanie przy pomocy biblioteki requests. 
#     Funkcja musi odczytać wielkość pobranej zawartości z nagłówka Content-Length lub zmierzyć długość response.content, 
#     a następnie wewnątrz sekcji krytycznej (with lock:) zaktualizować globalny licznik pobranych danych.

# Zarządzanie pulą wykonawczą: 
#     Krok 3. Użyj ThreadPoolExecutor z jawnym ograniczeniem max_workers=3 do przetworzenia listy adresów.
#     Zbierz wyniki przy użyciu as_completed(), aby przechwycić ewentualne błędy połączeń sieciowych (zamknięte w bloku try-except).
#     Wydrukuj końcowy raport zawierający sumaryczną liczbę pobranych bajtów.

# Kod szkieletowy do uzupełnienia dla Projektu 1:
# import concurrent.futures
# import requests
# import threading

# total_bytes_downloaded = 0
# bytes_lock = threading.Lock()

# URLS = [f"https://httpbin.org/bytes/{size}" for size in [500, 1200, 3500, 800, 2400]]

# def download_url(url: str):
#     global total_bytes_downloaded
#     # TODO: Zaimplementuj pobieranie, wyznacz długość danych i zaktualizuj total_bytes_downloaded przy użyciu bytes_lock
#     pass

# if __name__ == "__main__":
#     # TODO: Uruchom ThreadPoolExecutor, przekaż zadania i wyświetl total_bytes_downloaded po zakończeniu pracy
#     pass



# ROZWIĄZANIE:

import concurrent.futures
import requests
import threading

# Definiuję kody ANSI do zmiany koloru w terminalu
GREEN = '\033[92m'
RESET = '\033[0m'



# =========================================================
# KROK 1: Konfiguracja infrastruktury bazowej (ze szkieletu)
# =========================================================
total_bytes_downloaded = 0
bytes_lock = threading.Lock()

# URLS = [f"https://httpbin.org/bytes/{size}" for size in [500, 1200, 3500, 800, 2400]]
URLS = [f"https://jsonplaceholder.typicode.com/comments/{id}" for id in range(1, 6)]

# =========================================================
# KROK 2: Implementacja funkcji pobierającej
# =========================================================
def download_url(url: str):
    global total_bytes_downloaded
    
    # Wykonuję pojedyncze zapytanie przy pomocy biblioteki requests
    response = requests.get(url, timeout=5)
    
    # Podnoszę wyjątek w przypadku błędu HTTP (np. 404, 500), co przechwycę w Kroku 3
    response.raise_for_status()
    
    # Mierzę długość pobranej zawartości na podstawie response.content
    content_length = len(response.content)
    
    # Wchodzę do sekcji krytycznej, używając przygotowanego Locka
    with bytes_lock:
        # Bezpiecznie aktualizuję globalny licznik pobranych danych
        total_bytes_downloaded += content_length
        print(f"{GREEN}[{threading.current_thread().name}] Pobrałem {content_length} bajtów z adresu: {url}{RESET}")

# =========================================================
# KROK 3: Zarządzanie pulą wykonawczą
# =========================================================
if __name__ == "__main__":
    print(f"{GREEN}Rozpoczynam pracę puli wątków...\n{RESET}")
    
    # Używam ThreadPoolExecutor z jawnym ograniczeniem max_workers=3
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        
        # Przekazuję listę adresów do przetworzenia w puli zadań
        futures = {executor.submit(download_url, url): url for url in URLS}
        
        # Zbieram wyniki przy użyciu as_completed()
        for future in concurrent.futures.as_completed(futures):
            url = futures[future]
            
            # Zamykam odbiór wyników w bloku try-except, aby przechwycić błędy połączeń sieciowych
            try:
                # Odbieram wynik - jeśli funkcja download_url rzuciła błąd sieciowy, wybuchnie on właśnie w tym miejscu
                future.result()
            except requests.RequestException as exc:
                print(f"{GREEN}[BŁĄD SIECIOWY] Nie udało mi się pobrać danych z {url}. Szczegóły: {exc}{RESET}")
            except Exception as exc:
                print(f"{GREEN}[BŁĄD NIEZNANY] Wystąpił nieoczekiwany problem z {url}: {exc}{RESET}")

    # Wydruk końcowego raportu zawierającego sumaryczną liczbę pobranych bajtów
    print(f"\n{GREEN}--- RAPORT KOŃCOWY ---{RESET}")
    print(f"{GREEN}Wszystkie zadania zakończone. Całkowita liczba pobranych bajtów: {total_bytes_downloaded}{RESET}")