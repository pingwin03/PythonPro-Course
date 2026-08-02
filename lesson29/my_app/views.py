from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from celery.result import AsyncResult  # <--- Dodaję ten import, by sprawdzać status!
# Importuję moje zadania z pliku tasks.py znajdującego się w tym samym folderze
from .tasks import hello_world, multiply, log_timestamp, count_users, update_user_last_login, process_video, send_email_notification, progress_task # <--- Importuję moje nowe zadanie
from .tasks import fetch_nonexistent_url
from .models import EmailNotification
from .tasks import generate_users_csv # <--- Importuję moje nowe zadanie
from .models import UploadedImage
from .tasks import classify_image_task
from celery import chain
from .tasks import generate_random_number, multiply_by_10, save_result_to_file
from .tasks import send_priority_email, generate_random_number # Importuję stare i nowe zadanie
from django.db import transaction
from django.contrib.auth.models import User
import random
from .tasks import process_new_user
# Create your views here.


def trigger_hello_world(request):
    # Wywołuję moje zadanie asynchronicznie w tle za pomocą metody delay()
    hello_world.delay()
    
    # Natychmiast zwracam odpowiedź HTTP dla przeglądarki, nie czekając na workera
    return HttpResponse("Zadanie hello_world zostało poprawnie wysłane do kolejki Celery!")


def multiply_view(request):
    # Pobieram liczby 'a' i 'b' przekazane przez formularz w adresie URL[cite: 1]
    a = request.GET.get('a')
    b = request.GET.get('b')
    
    # Sprawdzam, czy obie liczby zostały podane (czyli czy formularz został wysłany)
    if a is not None and b is not None:
        # Wywołuję moje zadanie w tle, przekazując pobrane liczby jako argumenty[cite: 1]
        multiply.delay(a, b)
        
        # Zwracam natychmiastową odpowiedź do przeglądarki
        return HttpResponse(f"Wysłałem do Celery polecenie pomnożenia {a} przez {b}! Sprawdź konsolę workera.")

    # Jeśli użytkownik dopiero wszedł na stronę, przygotowuję i zwracam mu prosty formularz HTML[cite: 1]
    html_form = """
    <h2>Zadanie 2: Mnożenie w Celery</h2>
    <form method="get">
        <label>Liczba A: <input type="number" step="any" name="a" required></label><br><br>
        <label>Liczba B: <input type="number" step="any" name="b" required></label><br><br>
        <button type="submit">Pomnóż asynchronicznie</button>
    </form>
    """
    return HttpResponse(html_form)



def log_view(request):
    # Wywołuję zadanie asynchronicznie, przekazując je do Celery
    log_timestamp.delay()
    
    return HttpResponse("Polecenie zapisu do pliku zostało wysłane do Celery! Sprawdź folder polder projektu.")


def count_users_view(request):
    # Wysyłam zadanie do Celery
    count_users.delay()
    
    return HttpResponse("Zadanie zliczania użytkowników zostało wysłane. Sprawdź terminal workera!")


def update_login_view(request):
    # Wywołuję zadanie i przekazuję mu argument (np. ID = 1)
    # Zamiast w nawiasach zwykłych, argument podaję w nawiasach od .delay()
    update_user_last_login.delay(1)
    
    return HttpResponse("Wysłano zadanie aktualizacji czasu logowania dla użytkownika ID=1!")


def process_video_view(request):
    # Wywołuję moje zadanie w tle używając .delay()
    process_video.delay()
    
    # Przeglądarka nie czeka 15 sekund! Od razu zwracam komunikat do użytkownika
    return HttpResponse("Przetwarzanie wideo rozpoczęte!")

def trigger_email_view(request):
    # 1. Tworzę nowy wpis w bazie danych (data wysłania pozostaje pusta)
    notification = EmailNotification.objects.create(
        recipient_email="test@example.com",
        subject="Witaj w systemie!",
        body="To jest testowa wiadomość."
    )
    
    # 2. Przekazuję ID nowo utworzonego obiektu do zadania w tle
    send_email_notification.delay(notification.id)
    
    # Od razu zwracam odpowiedź do użytkownika
    return HttpResponse(f"Zadanie wysłania maila zostało dodane do kolejki! ID powiadomienia: {notification.id}")



def start_progress_view(request):
    # Uruchamiam zadanie w tle
    task = progress_task.delay()
    
    # Zwracam ID mojego zadania, abym mógł go użyć w drugim endpoincie
    return JsonResponse({'task_id': task.id})

def task_status_view(request, task_id):
    # Odpytuję Celery o zadanie używając dostarczonego task_id
    result = AsyncResult(task_id)
    
    # Sprawdzam, w jakim stanie jest moje zadanie i odpowiednio buduję słownik
    if result.state == 'PROGRESS':
        response_data = {
            'state': result.state,
            'current': result.info.get('current', 0),
            'total': result.info.get('total', 100),
        }
    elif result.state == 'SUCCESS':
        response_data = {
            'state': result.state,
            'current': 100,
            'total': 100,
            # Wynik zwracany przez return w moim zadaniu trafia do result.info
            'status': result.info.get('status', 'Zakończone') 
        }
    else:
        # PENDING lub inne stany początkowe/błędów
        response_data = {
            'state': result.state,
            'current': 0,
            'total': 100,
        }
        
    # Zwracam gotowe dane postępu do przeglądarki jako JSON
    return JsonResponse(response_data)



def start_csv_report_view(request):
    # Uruchamiam zadanie asynchronicznie
    task = generate_users_csv.delay()
    
    # Zwracam ID mojego zadania do przeglądarki
    return JsonResponse({'task_id': task.id, 'status': 'Zadanie rozpoczęte'})

def check_csv_report_view(request, task_id):
    # Sprawdzam stan mojego zadania za pomocą jego ID
    result = AsyncResult(task_id)
    
    if result.state == 'SUCCESS':
        # Gdy zadanie się zakończyło, jego "return" ląduje w zmiennej result.result
        download_url = result.result
        return JsonResponse({
            'state': result.state,
            'download_url': download_url,
            'message': 'Plik jest gotowy do pobrania!'
        })
    elif result.state == 'FAILURE':
        return JsonResponse({
            'state': result.state,
            'error': str(result.info) # Informacja o błędzie
        })
    else:
        # PENDING lub PROGRESS
        return JsonResponse({
            'state': result.state,
            'message': 'Plik wciąż się generuje, proszę czekać...'
        })
        
        
def start_retry_task_view(request):
    # Odpalam moje wadliwe zadanie w tle
    fetch_nonexistent_url.delay()
    
    # Zwracam informację do przeglądarki
    return JsonResponse({
        'status': 'Zadanie wystartowało',
        'message': 'Spójrz w terminal Workera Celery. Zobaczysz tam pierwszą próbę, a za 60 sekund kolejną!'
    })
    
    
def upload_image_view(request):
    if request.method == 'POST' and request.FILES.get('image'):
        # Tworzę nowy wpis w bazie i zapisuję obrazek na dysk
        new_img = UploadedImage.objects.create(
            image=request.FILES['image']
        )
        
        # Uruchamiam asynchronicznie moją analizę - przekazuję tylko ID!
        classify_image_task.delay(new_img.id)
        
        # Zabezpieczam przed podwójnym wysłaniem formularza przez odświeżenie (Redirect po POST)
        return redirect('upload_image')

    # Pobieram wszystkie obrazki, najnowsze na górze
    images = UploadedImage.objects.all().order_by('-id')
    return render(request, 'upload_image.html', {'images': images})



def start_chain_view(request):
    # Buduję mój łańcuch używając sygnatur .s()
    # Zauważ, że w .s() do zadań 2 i 3 nie wpisuję żadnych argumentów - Celery samo "wepnie" tam wyniki z poprzednich kroków.
    my_workflow = chain(
        generate_random_number.s(),
        multiply_by_10.s(),
        save_result_to_file.s()
    )
    
    # Uruchamiam cały zestaw jednym poleceniem (można też użyć my_workflow.apply_async())
    my_workflow()

    # Odpowiadam użytkownikowi, żeby wiedział, że proces ruszył
    return JsonResponse({
        'status': 'Sukces',
        'message': 'Łańcuch zadań został wystrzelony! Zobacz konsolę Workera i plik chain_results.txt w folderze media.'
    })
    
def test_queues_view(request):
    # 1. Odpalam zwykłe zadanie (Celery samo wrzuci je na 'default')
    generate_random_number.delay()
    
    # 2. Odpalam ważne zadanie (Zgodnie z settings.py trafi do 'priority_queue')
    send_priority_email.delay("prezes@mojafirma.pl")
    
    # Odpowiadam użytkownikowi
    return JsonResponse({
        'status': 'Zadania wysłane do dwóch różnych kolejek!',
        'message': 'Spójrz w terminale swoich workerów - każdy powinien przejąć inne zadanie.'
    })    
    
    
def create_user_with_transaction(request):
    random_id = random.randint(1000, 9999)
    username = f"nowy_user_{random_id}"
    
    # Otwieramy transakcję atomową
    with transaction.atomic():
        # 1. Tworzymy obiekt w bazie (na razie widoczny tylko w tej transakcji)
        new_user = User.objects.create_user(username=username, password='password123')
        
        # 2. Zlecamy zadanie DOPIERO, gdy transakcja pomyślnie się zapisze
        transaction.on_commit(lambda: process_new_user.delay(new_user.id))
        
    return HttpResponse(f"Zapisano użytkownika {username}. Zadanie przetwarzania zostało poprawnie zakolejkowane.")