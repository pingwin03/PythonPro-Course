# Zadanie 15 – Obsługa błędów i ponawianie
# Stwórz zadanie, które próbuje połączyć się z nieistniejącym adresem URL. Oczywiście rzuci
# to wyjątek. Skonfiguruj zadanie tak, aby w przypadku błędu ponawiało próbę 3 razy w
# odstępach 1-minutowych.Tip
# Użyj try...except oraz self.retry(countdown=60, max_retries=3).


# Zadanie w my_app/tasks.py


import requests # Upewniam się, że mam zaimportowaną tę bibliotekę
from celery import shared_task

# ... moje poprzednie zadania ...

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
    
    
# Widok testowy w my_app/views.py    

from .tasks import fetch_nonexistent_url

# ... moje poprzednie widoki ...

def start_retry_task_view(request):
    # Odpalam moje wadliwe zadanie w tle
    fetch_nonexistent_url.delay()
    
    # Zwracam informację do przeglądarki
    return JsonResponse({
        'status': 'Zadanie wystartowało',
        'message': 'Spójrz w terminal Workera Celery. Zobaczysz tam pierwszą próbę, a za 60 sekund kolejną!'
    })
    
    
    
# Ścieżka w my_project/urls.py



    # Ścieżka do testowania ponawiania zadań z Zadania 15
    path('test-retry/', views.start_retry_task_view, name='start_retry'),
    
    
# Testowanie:
    
celery -A my_project worker -l info -P solo
python manage.py runserver


http://127.0.0.1:8000/test-retry/    Przeglądarka pokazała JSON z potwierdzeniem.
  Widzę, że Worker próbuje wykonać zadanie, pokazuje błąd połączenia i wypisuje komunikat o ponawianiu. 
  Teraz czekam minutę (countdown=60). Po minucie Worker automatycznie prubuję ponownie,
  a liczba prób (self.request.retries) się zwiększy! Po 3 próbach ostatecznie się podda i zadanie przyjmie status FAILURE 