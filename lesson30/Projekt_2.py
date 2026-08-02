# Projekt 2: Równoległy Generator Paczek Raportowych (CPU-bound)
# Zaprojektuj system dzielący duży zakres liczb na paczki (chunks) i wyznaczający dla każdej liczby, 
# czy jest ona liczbą pierwszą. Obliczenia muszą zostać zrównoleglone na wszystkie rdzenie procesora maszyny.

# Wymagania implementacyjne:
# 1. Zaimplementuj czysto matematyczną, nieoptymalną funkcję is_prime(n), która sprawdza podzielność liczby 
# pętlą for od 2 do $\sqrt{n}$ (klasyczne zadanie obciążające CPU).
# 2. Przygotuj funkcję process_range(start, end), która iteruje po podanym przedziale i zwraca listę 
# znalezionych liczb pierwszych.
# 3. W funkcji głównej przygotuj duży zakres (np. od 1 000 000 do 1 500 000) 
# i podziel go na równe fragmenty odpowiadające liczbie rdzeni CPU w systemie (pobierz ją przez multiprocessing.cpu_count()).
# 4. Wykorzystaj ProcessPoolExecutor do równoległego uruchomienia obliczeń dla wszystkich fragmentów.
# 5. Złącz wyniki cząstkowe z procesów w jedną listę końcową i zmierz całkowity czas wykonania obliczeń.


# Kod szkieletowy do uzupełnienia dla Projektu 2:
# from concurrent.futures import ProcessPoolExecutor
# import math
# import time
# import multiprocessing

# def is_prime(n: int) -> bool:
#     if n < 2: return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0: return False
#     return True

# def process_range(bounds: tuple) -> list:
#     start, end = bounds
#     # TODO: Przetwórz przedział i zwróć listę znalezionych liczb pierwszych
#     return []

# if __name__ == "__main__":
#     start_num = 1_000_000
#     end_num = 1_300_000
#     cpus = multiprocessing.cpu_count()
    
#     # TODO: Przygotuj listę krotek z przedziałami (bounds) dopasowaną do liczby procesorów (cpus)
#     # TODO: Uruchom ProcessPoolExecutor, przetwórz dane i porównaj czas pracy ze schematem jednowątkowym
#     pass


from concurrent.futures import ProcessPoolExecutor
import math
import time
import multiprocessing

# Definiuję kody ANSI dla lepszej czytelności w terminalu
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

# =========================================================
# KROK 1: Implementuję czysto matematyczną, nieoptymalną funkcję is_prime(n)
# =========================================================
def is_prime(n: int) -> bool:
    if n < 2: return False
    # Sprawdzam podzielność klasyczną, nieoptymalną pętlą dla obciążenia CPU
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

# =========================================================
# KROK 2: Przygotowuję funkcję process_range(start, end)
# =========================================================
def process_range(bounds: tuple) -> list:
    start, end = bounds
    primes = []
    
    # Przetwarzam otrzymany przedział liczbowy
    for num in range(start, end):
        # Wywołuję funkcję obciążającą procesor i dodaję liczbę do listy
        if is_prime(num):
            primes.append(num)
            
    # Zwracam listę wyliczoną przez ten konkretny proces worker'a
    return primes

if __name__ == "__main__":
    # =========================================================
    # KROK 3: Przygotowuję duży zakres i dzielę go na fragmenty wg rdzeni CPU
    # =========================================================
    start_num = 1_000_000
    end_num = 1_300_000
    
    # Pobieram liczbę dostępnych rdzeni procesora w systemie
    cpus = multiprocessing.cpu_count()
    
    print(f"{CYAN}Rozpoczynam analizę przedziału od {start_num} do {end_num}...{RESET}")
    print(f"{CYAN}Wykryłem {cpus} logicznych rdzeni procesora. Dzielę zadanie na {cpus} paczek.{RESET}\n")
    
    bounds_list = []
    # Obliczam rozmiar jednej paczki tak, aby równo obdzielić wszystkie procesy
    chunk_size = math.ceil((end_num - start_num) / cpus)
    
    for i in range(cpus):
        chunk_start = start_num + i * chunk_size
        # Zabezpieczam się, by nie wyjść poza górną granicę przedziału
        chunk_end = min(chunk_start + chunk_size, end_num)
        
        if chunk_start < end_num:
            # Tworzę krotki z przedziałami gotowe do przekazania
            bounds_list.append((chunk_start, chunk_end))

    # --- Blok testowy podejścia jednowątkowego (do wyliczenia zysku wydajności) ---
    print(f"{YELLOW}--- TEST JEDNOPROCESOWY (Tradycyjny) ---{RESET}")
    start_time_single = time.time()
    single_results = process_range((start_num, end_num))
    end_time_single = time.time()
    single_duration = end_time_single - start_time_single
    print(f"{YELLOW}Znalazłem {len(single_results)} liczb pierwszych.{RESET}")
    print(f"{YELLOW}Czas pracy: {single_duration:.2f} sekund{RESET}\n")

    print(f"{GREEN}--- TEST WIELOPROCESOWY (Zgodny z zadaniem) ---{RESET}")
    
    # Zaczynam pomiar całkowitego czasu pracy wieloprocesowej (część Kroku 5)
    start_time_multi = time.time()
    multi_results = []
    
    # =========================================================
    # KROK 4: Wykorzystuję ProcessPoolExecutor do równoległego uruchomienia
    # =========================================================
    # Otwieram pulę procesów ograniczoną do liczby dostępnych rdzeni
    with ProcessPoolExecutor(max_workers=cpus) as executor:
        # Zlecam równoległe przetwarzanie - mapuję funkcję process_range na przygotowane krotki
        results = executor.map(process_range, bounds_list)
        
        # =========================================================
        # KROK 5: Złączam wyniki cząstkowe i mierzę całkowity czas obliczeń
        # =========================================================
        # Zbieram wyniki cząstkowe z każdego procesu i łączę w jedną wielką listę końcową
        for chunk_of_primes in results:
            multi_results.extend(chunk_of_primes)
            
    # Kończę pomiar czasu
    end_time_multi = time.time()
    multi_duration = end_time_multi - start_time_multi
    
    # Wyświetlam ostateczne wyniki i zmierzony czas
    print(f"{GREEN}Znalazłem {len(multi_results)} liczb pierwszych.{RESET}")
    print(f"{GREEN}Czas pracy: {multi_duration:.2f} sekund{RESET}\n")
    
    # Zestawienie wyników
    if multi_duration > 0:
        speedup = single_duration / multi_duration
        print(f"{CYAN}PODSUMOWANIE: Wykorzystanie wielu rdzeni procesora przyspieszyło kod {speedup:.2f} razy!{RESET}")