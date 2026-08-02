# Zadanie 14 – Generowanie raportu CSV
# Napisz zadanie, które generuje plik CSV ze wszystkimi użytkownikami i ich adresami email.
# Plik powinien być zapisany w katalogu media. Widok, który inicjuje to zadanie, powinien
# zwrócić task_id. Stwórz drugi widok, który pozwala sprawdzić, czy zadanie się zakończyło,
# a jeśli tak, udostępnia link do pobrania pliku.

# Konfiguracja katalogu Media (my_project/settings.py)

import os

# ... reszta pliku settings.py ...

# Adres URL, pod którym będą widoczne pliki w przeglądarce
MEDIA_URL = '/media/'

# Fizyczna ścieżka na dysku, gdzie Django stworzy folder "media"
MEDIA_ROOT = BASE_DIR / 'media'

# my_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings # <--- Importuję moje ustawienia
from django.conf.urls.static import static # <--- Importuję funkcję static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls')),
]

# Pozwalam Django na serwowanie plików z folderu media w trybie deweloperskim
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
    
# Logika generowania CSV w Celery (my_app/tasks.py)

import csv
import os
import time
from django.conf import settings
from django.contrib.auth.models import User
from celery import shared_task

# ... moje poprzednie zadania ...

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


# Widoki obsługujące proces (my_app/views.py)

from django.http import JsonResponse
from celery.result import AsyncResult
from .tasks import generate_users_csv # <--- Importuję moje nowe zadanie

# ... moje poprzednie widoki ...

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
        
# Rejestracja adresów URL (my_project/urls.py)

from django.contrib import admin
from django.urls import path
from django.conf import settings # <--- Importuję moje ustawienia
from django.conf.urls.static import static # <--- Importuję funkcję static
from my_app import views # <--- Importuję moje widoki

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # ... (tutaj masz pewnie swoje poprzednie ścieżki z Zadań 1-11) ...
    
    # Dodaję ścieżki do obsługi paska postępu z Zadania 11
    path('start-progress/', views.start_progress_view, name='start_progress'),
    path('task-status/<str:task_id>/', views.task_status_view, name='task_status'),
    
    # Dodaję nowe ścieżki do generowania raportu CSV z Zadania 14
    path('start-csv/', views.start_csv_report_view, name='start_csv'),
    path('check-csv/<str:task_id>/', views.check_csv_report_view, name='check_csv'),
]

# Pozwalam Django na serwowanie plików z mojego folderu media w trybie deweloperskim
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# test:

# celery -A my_project worker -l info -P solo - aby zaczytał kod nowego zadania

# http://127.0.0.1:8000/start-csv/    - skopiuj wygenerowane task_id

# http://127.0.0.1:8000/check-csv/SKOPIOWANE_ID/
# dostaje w odpowiedzi JSON klucz "download_url"
# http://127.0.0.1:8000/media/users_report_...csv, plik pobierze się na Twój komputer!
