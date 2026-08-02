# Zadanie 11 – Śledzenie postępu zadania
# Stwórz zadanie, które w pętli od 1 do 100 wykonuje jakąś operację, śpiąc 0.1 sekundy w
# każdej iteracji. Po każdej iteracji zadanie powinno aktualizować swój stan, informując o
# postępie. Stwórz drugi endpoint w Django (/task-status/<task_id>/), który będzie zwracał
# aktualny postęp zadania.Tip
# Użyj self.update_state(state='PROGRESS', meta={'current': i, 'total': 100}) wewnątrz
# zadania. Będziesz musiał związać zadanie z instancją (@shared_task(bind=True)).


# Definicja zadania z postępem (my_app/tasks.py)
from celery import shared_task
import time

# ... Moje poprzednie zadania ...

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


# Widoki do uruchamiania i sprawdzania statusu (my_app/views.py)

from django.http import JsonResponse
from celery.result import AsyncResult  # <--- Dodaję ten import, by sprawdzać status!

from .models import EmailNotification
from .tasks import (
    hello_world, multiply, log_timestamp, count_users, 
    update_user_last_login, process_video, send_email_notification,
    progress_task # <--- Importuję moje nowe zadanie
)

# ... Moje poprzednie widoki ...

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


# Ścieżki URL (my_project/urls.py)

from django.urls import path
from my_app import views

urlpatterns = [
    # ... moje poprzednie ścieżki ...
    path('start-progress/', views.start_progress_view, name='start_progress'),
    path('task-status/<str:task_id>/', views.task_status_view, name='task_status'),
]

testy :
    celery -A my_project worker -l info -P solo
    http://127.0.0.1:8000/start-progress/
    
 Sprawdzam postęp: Otwóram szybko nową zakładkę z adresem   
 http://127.0.0.1:8000/task-status/TWOJE_SKOPIOWANE_ID/
 Odświeżam stronę: Odświeżając stronę w ciągu tych pierwszych 10 sekund, widać,
 jak rośnie wartość parametru current w odpowiedzi JSON. 
 Po upływie tego czasu parametr state zmieni się na SUCCESS.