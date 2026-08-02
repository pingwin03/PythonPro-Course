# Zadanie 18 – Różne kolejki zadań
# Skonfiguruj dwie różne kolejki: default dla większości zadań i priority_queue dla zadań
# krytycznych. Stwórz zadanie do wysyłania maila i skonfiguruj je tak, aby zawsze trafiało do
# priority_queue. Uruchom dwa workery: jeden nasłuchujący na kolejce domyślnej, a drugi na
# priorytetowej.

# Konfiguracja kolejek w my_project/settings.py

# --- USTAWIENIA CELERY ---
# (tu zostawiam dotychczasowe ustawienia brokera,  CELERY_BROKER_URL itp.)

# Określam nazwę domyślnej kolejki, do której wpadają wszystkie "zwykłe" zadania
CELERY_TASK_DEFAULT_QUEUE = 'default'

# Definiuję specjalne trasy (routing). 
# Celery z automatu utworzy tę kolejkę w Redis, gdy tylko wyślę do niej pierwsze zadanie.
CELERY_TASK_ROUTES = {
    # Mówię: "Jeśli wywołuję zadanie 'send_priority_email' w aplikacji 'my_app', 
    # wrzuć je zawsze do kolejki 'priority_queue'"
    'my_app.tasks.send_priority_email': {'queue': 'priority_queue'},
}


# Tworzę priorytetowe zadanie w my_app/tasks.py

import time
from celery import shared_task

# ... moje poprzednie zadania ...

@shared_task
def send_priority_email(email_address):
    # Symuluję pracę nad ważnym zadaniem
    print(f"\n[PRIORYTET] Przygotowuję maila do: {email_address}...")
    time.sleep(2) # udaję, że trwa łączenie z serwerem SMTP
    print(f"[PRIORYTET] ✅ Ważny e-mail do {email_address} został wysłany!")
    
    return f"Wysłano maila do {email_address}"


# Tworzę widok do testowania w my_app/views.py


from django.http import JsonResponse
from .tasks import send_priority_email, generate_random_number # Importuję stare i nowe zadanie

# ... moje poprzednie widoki ...

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
    
    
# Dopisuję ścieżkę w my_project/urls.py    


path('test-queues/', views.test_queues_view, name='test_queues'),



Testy:
Teraz muszę uruchomić serwer Django i DWA osobne terminale dla Celery. W każdym z terminali oczywiście muszę mieć aktywne środowisko wirtualne.
.\venv\Scripts\Activate.ps1


Terminal 1:   python manage.py runserver

# Worker dla "zwykłych" zadań
Terminal 2:    celery -A my_project worker -l info -Q default -P solo

# Worker dla zadań "krytycznych":
Terminal 3: celery -A my_project worker -l info -Q priority_queue -P solo   
 
 
http://127.0.0.1:8000/test-queues/ 

# Gdy spojrzę na Terminal 2, zobaczę, że wykonał zadanie generate_random_number. Kompletnie zignorował maila.
# Gdy spojrzę na Terminal 3, zobaczę, że to on, i tylko on, odebrał zadanie send_priority_email.
# W ten sposób zadania krytyczne (takie jak maile) nigdy nie utkną za zadaniami pobocznymi!