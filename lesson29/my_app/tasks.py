
import datetime
import time  # <--- Importuję bibliotekę time na górze pliku
from celery import shared_task
# Importuję wbudowany model użytkownika Django
from django.contrib.auth.models import User
from django.utils import timezone  # <--- Dodaję ten import na górze pliku
from .models import EmailNotification  # <--- Importuję mój nowy model
from datetime import timedelta
from .models import LogEntry # <--- Importuję mój nowy model
import requests
from bs4 import BeautifulSoup
from celery import shared_task
from .models import ScrapedWebsite # <--- Importuję mój nowy model
import csv
import os
import time
from django.conf import settings
from django.contrib.auth.models import User
from .models import UploadedImage
from PIL import Image
import random


# Tutaj będę definiować wszystkie moje asynchroniczne zadania, zaczynając od hello_world

@shared_task
def hello_world():
    # Drukuję w konsoli mojego workera wymagany napis "Hello from Celery!"
    print("Hello from Celery!")
    
    
@shared_task
def multiply(a, b):
    # Rzutuję argumenty na typ zmiennoprzecinkowy (float), na wypadek gdyby dotarły jako tekst
    wynik = float(a) * float(b)
    
    # Drukuję wynik w konsoli workera, abym mógł łatwo zweryfikować działanie
    print(f"Obliczyłem iloczyn: {a} * {b} = {wynik}")
    
    # Zwracam wynik zgodnie z poleceniem
    return wynik

@shared_task
def log_timestamp():
    # Pobieram aktualną datę i godzinę i formatuję ją do czytelnej postaci
    teraz = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Otwieram plik log.txt w trybie dopisywania ('a' - append). 
    # Jeśli plik nie istnieje, Python sam go utworzy w głównym folderze projektu.
    with open("log.txt", "a", encoding="utf-8") as plik:
        plik.write(f"Log wygenerowany przez Celery: {teraz}\n")
        
    # Dodatkowo drukuję informację w konsoli workera dla łatwiejszej weryfikacji
    print(f"Zapisano czas {teraz} do pliku log.txt")
    
    return teraz


@shared_task
def count_users():
    # Pobieram liczbę wszystkich użytkowników z bazy danych
    liczba = User.objects.count()
    
    # Drukuję wynik w konsoli workera, tak jak w poleceniu
    print(f"Aktualna liczba użytkowników w bazie: {liczba}")
    
    return liczba



@shared_task
def update_user_last_login(user_id):
    try:
        # 1. Szukam użytkownika o podanym ID w bazie danych
        user = User.objects.get(id=user_id)
        
        # 2. Aktualizuję pole last_login na dokładny, obecny czas
        user.last_login = timezone.now()
        
        # 3. Zapisuję zmiany w bazie
        user.save()
        
        print(f"Sukces: Zaktualizowano czas logowania dla użytkownika {user.username} (ID: {user_id})")
        return True
        
    except User.DoesNotExist:
        # Obsługuję błąd na wypadek, gdybym podał ID, którego nie ma w bazie
        print(f"Błąd: Użytkownik o ID {user_id} nie istnieje w bazie danych.")
        return False
    
    
    
@shared_task
def process_video():
    print("Rozpoczynam przetwarzanie wideo...")
    
    # Symuluję ciężką pracę, zatrzymując działanie zadania na 15 sekund
    time.sleep(15)
    
    print("Sukces: Przetwarzanie wideo zakończone!")
    return True




@shared_task
def send_email_notification(notification_id):
    try:
        # 1. Pobieram powiadomienie z bazy na podstawie otrzymanego ID
        notification = EmailNotification.objects.get(id=notification_id)
        
        print(f"Rozpoczynam wysyłanie maila do {notification.recipient_email}...")
        
        # 2. Symuluję proces wysyłania maila (np. 5 sekund opóźnienia)
        time.sleep(5)
        
        # 3. Aktualizuję pole sent_at na dokładny, obecny czas
        notification.sent_at = timezone.now()
        
        # 4. Zapisuję zmiany w bazie danych
        notification.save()
        
        print(f"Sukces: Mail wysłany! Zaktualizowano czas wysyłki dla ID {notification_id}.")
        return True
        
    except EmailNotification.DoesNotExist:
        # Obsługuję sytuację, w której powiadomienie o tym ID nie istnieje w bazie
        print(f"Błąd: Powiadomienie o ID {notification_id} nie istnieje.")
        return False
    
    
# Dodaję bind=True, aby funkcja miała dostęp do instancji zadania (jako argument self)
@shared_task(bind=True)
def progress_task(self):
    print("Rozpoczynam zadanie ze śledzeniem postępu...")
    
    # Wykonuję pętlę od 1 do 100 (włącznie)
    for i in range(1, 101):
        # Symuluję pracę zasypiając na 0.1 sekundy w każdej iteracji
        time.sleep(0.1)
        
        # Aktualizuję własny stan zadania, przekazując metadane z postępem
        self.update_state(
            state='PROGRESS', 
            meta={'current': i, 'total': 100}
        )
        
    # Gdy pętla się zakończy, zwracam ostateczny wynik
    print("Sukces: Zadanie zakończone!")
    return {'current': 100, 'total': 100, 'status': 'Zakończone!'}




@shared_task
def cleanup_old_logs():
    print("Rozpoczynam czyszczenie starych logów...")
    
    # Obliczam graniczną datę (obecny czas minus 90 dni)
    threshold_date = timezone.now() - timedelta(days=90)
    
    # Filtruję obiekty, w których 'created_at' jest mniejsze (starsze) niż threshold_date
    # Metoda delete() zwraca krotkę, z której interesuje mnie tylko pierwsza wartość (ilość usuniętych)
    deleted_count, _ = LogEntry.objects.filter(created_at__lt=threshold_date).delete()
    
    print(f"Zakończono sprzątanie. Usunięto {deleted_count} wpisów.")
    return deleted_count




@shared_task
def scrape_example_com():
    print("Rozpoczynam pobieranie tytułu ze strony example.com...")
    
    url = 'https://example.com'
    
    # Pobieram zawartość strony używając biblioteki requests
    response = requests.get(url)
    
    # Upewniam się, że żądanie zakończyło się sukcesem (status 200)
    response.raise_for_status()
    
    # Parsuję kod HTML pobranej strony za pomocą BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Wyciągam zawartość znacznika <title>. Jeśli go nie ma, ustawiam wartość domyślną.
    page_title = soup.title.string if soup.title else "Brak tytułu"
    
    # Zapisuję wyciągnięty tytuł do mojej bazy danych
    ScrapedWebsite.objects.create(title=page_title)
    
    print(f"Sukces! Zapisano tytuł: {page_title}")
    
    return page_title


@shared_task
def generate_users_csv():
    print("Rozpoczynam generowanie raportu CSV...")
    
    # Upewniam się, że folder "media" w ogóle istnieje na moim dysku
    os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
    
    # Tworzę unikalną nazwę pliku, dodając znacznik czasu (timestamp) 
    # żeby stare raporty nie były nadpisywane przez nowe
    filename = f"users_report_{int(time.time())}.csv"
    
    # Buduję pełną, fizyczną ścieżkę do pliku
    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    
    # Otwieram plik i zaczynam wpisywać do niego dane
    with open(filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Wpisuję pierwszy wiersz, czyli nagłówki kolumn
        writer.writerow(['ID', 'Username', 'Email'])
        
        # Pobieram wszystkich użytkowników z bazy danych
        users = User.objects.all()
        
        # Przechodzę pętlą po użytkownikach i wpisuję ich do CSV
        for user in users:
            writer.writerow([user.id, user.username, user.email])
            
    print(f"Sukces! Raport został wygenerowany: {filename}")
    
    # Zwracam URL do pliku (np. "/media/users_report_1690000000.csv"), 
    # by mój drugi widok mógł go odebrać
    return f"{settings.MEDIA_URL}{filename}"


# Dodaję bind=True, abym mógł odnosić się do instancji tego zadania poprzez 'self'
@shared_task(bind=True)
def fetch_nonexistent_url(self):
    url = "http://adres-ktory-na-100-procent-nie-istnieje-w-internecie.com"
    
    # Wyświetlam w konsoli informację, która to już próba.
    # self.request.retries przechowuje liczbę dotychczasowych nieudanych prób (zaczyna od 0).
    print(f"\n[Podejście {self.request.retries + 1}] Próbuję pobrać dane z: {url}")
    
    try:
        # Próbuję nawiązać połączenie (co oczywiście z góry jest skazane na porażkę)
        response = requests.get(url, timeout=5)
        response.raise_for_status() # Jeśli kod statusu to np. 404 lub 500, to rzuci wyjątkiem
        return "Udało się! (To się nigdy nie wypisze)"
        
    except requests.exceptions.RequestException as exc:
        print(f"Błąd połączenia: {exc}")
        print("Uruchamiam procedurę ponawiania (retry)...")
        
        # Złapałem błąd sieciowy, więc mówię Celery:
        # "Spróbuj jeszcze raz za 60 sekund. Maksymalnie daję Ci 3 szanse."
        # Zwracam uwagę na słówko 'raise' - self.retry to tak naprawdę specjalny wyjątek, 
        # który Celery musi przechwycić, żeby zaplanować zadanie na nowo.
        raise self.retry(exc=exc, countdown=60, max_retries=3)
    
    
@shared_task
def classify_image_task(image_id):
    # 1. Pobieram mój obraz z bazy danych na podstawie przekazanego ID
    try:
        img_obj = UploadedImage.objects.get(id=image_id)
    except UploadedImage.DoesNotExist:
        return "Błąd: Obraz nie istnieje w bazie."

    # 2. Otwieram fizyczny plik na moim dysku. 
    # img_obj.image.path zwraca pełną, fizyczną ścieżkę w systemie Windows
    try:
        with Image.open(img_obj.image.path) as img:
            width, height = img.size
            mode = img.mode  # Np. 'RGB' dla kolorowych, 'L' dla czarno-białych
            
            # Prosta "klasyfikacja"
            if mode in ['RGB', 'RGBA']:
                color_type = "Kolorowy"
            elif mode == 'L':
                color_type = "Skala szarości (czarno-biały)"
            else:
                color_type = f"Inny (tryb {mode})"
                
            # Formatuję mój wynik
            result = f"Rozmiar: {width}x{height}px, Kolor: {color_type}"
            
    except Exception as e:
        result = f"Błąd podczas analizy: {str(e)}"
        
    # 3. Zapisuję wynik w bazie danych
    img_obj.classification_result = result
    img_obj.save()
    
    # Zwracam też wynik tekstowy, żeby był widoczny w logach Workera
    return f"Zakończono analizę obrazu {image_id}: {result}"


@shared_task
def generate_random_number():
    # Krok 1: Losuję liczbę
    number = random.randint(1, 100)
    print(f"\n[Łańcuch - Krok 1] Wylosowałem: {number}")
    
    # Zwracam ją - Celery automatycznie przekaże ją do kolejnego zadania!
    return number

@shared_task
def multiply_by_10(number):
    # Krok 2: Przyjmuję 'number' z poprzedniego zadania i mnożę
    result = number * 10
    print(f"[Łańcuch - Krok 2] Pomnożyłem {number} x 10. Wynik to: {result}")
    
    # Zwracam wynik - Celery wrzuci go do kroku nr 3!
    return result

@shared_task
def save_result_to_file(final_result):
    # Krok 3: Przyjmuję wynik i zapisuję go na dysku
    # Używam MEDIA_ROOT, żeby zapisać to w E:\PythonPro-Course\homework\lesson29\media\
    file_path = os.path.join(settings.MEDIA_ROOT, 'chain_results.txt')
    
    # Otwieram plik w trybie 'a' (append), żeby dopisywać kolejne wyniki na końcu
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f"Wynik dzialania lancucha: {final_result}\n")
        
    print(f"[Łańcuch - Krok 3] Zapisano {final_result} w pliku {file_path}")
    return "Łańcuch zakończony sukcesem!"


@shared_task
def send_priority_email(email_address):
    # Symuluję pracę nad ważnym zadaniem
    print(f"\n[PRIORYTET] Przygotowuję maila do: {email_address}...")
    time.sleep(2) # udaję, że trwa łączenie z serwerem SMTP
    print(f"[PRIORYTET] ✅ Ważny e-mail do {email_address} został wysłany!")
    
    return f"Wysłano maila do {email_address}"



@shared_task
def process_new_user(user_id):
    # Symulujemy krótkie przetwarzanie
    time.sleep(1)
    
    try:
        user = User.objects.get(id=user_id)
        return f"SUKCES: Przetworzono użytkownika o loginie: {user.username}"
    except User.DoesNotExist:
        return f"BŁĄD: Użytkownik o ID {user_id} nie istnieje w bazie!"

