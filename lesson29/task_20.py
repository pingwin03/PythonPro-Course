# Zadanie 20 – Transakcje bazodanowe i zadania
# Stwórz widok, który w ramach transakcji atomowej (@transaction.atomic) tworzy nowy
# obiekt w bazie i następnie wywołuje zadanie Celery, które ma ten obiekt przetworzyć.
# Dlaczego ważne jest, aby wywołać zadanie po pomyślnym zatwierdzeniu transakcji? Jak
# można to zapewnić?Tip
# Poszukaj informacji o transaction.on_commit.



# Zadanie w Celery (my_app/tasks.py)

from celery import shared_task
from django.contrib.auth.models import User
import time

@shared_task
def process_new_user(user_id):
    # Symulujemy krótkie przetwarzanie
    time.sleep(1)
    
    try:
        user = User.objects.get(id=user_id)
        return f"SUKCES: Przetworzono użytkownika o loginie: {user.username}"
    except User.DoesNotExist:
        return f"BŁĄD: Użytkownik o ID {user_id} nie istnieje w bazie!"
    
    
# Widok z transakcją (my_app/views.py)    


from django.http import HttpResponse
from django.db import transaction
from django.contrib.auth.models import User
import random
from .tasks import process_new_user

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


# Podłączenie adresu (my_project/urls.py)


from django.urls import path
from my_app.views import create_user_with_transaction

urlpatterns = [
    # ... twoje poprzednie ścieżki ...
    path('test-transaction/', create_user_with_transaction, name='test_transaction'),
]


test:
    o zapisaniu plików, zrestartuj dla pewności Workera Celery 
    (żeby wczytał nową funkcję z tasks.py), odpal serwer Django i wejdź na [http://127.0.0.1:8000/test-transaction/]
    
    
    
# Dlaczego to takie ważne? (Teoria)
# Wyobraź sobie, że tworzysz obiekt w bazie danych wewnątrz transakcji (@transaction.atomic), 
# a zaraz potem w tej samej funkcji wywołujesz zadanie Celery, przekazując mu ID tego nowego obiektu.

# Pojawia się tutaj problem tzw. wyścigu (race condition):

# Celery jest niezwykle szybkie. Zadanie trafia do brokera (Redis) natychmiast i Worker często zaczyna je wykonywać w ułamku sekundy.

# Tymczasem Twoja funkcja w Django jeszcze się nie skończyła, więc transakcja bazodanowa nie została zatwierdzona (skmitowana).

# Worker Celery próbuje pobrać z bazy danych obiekt po jego ID. Ponieważ ma własne, osobne połączenie z bazą, nie widzi jeszcze tego uncommitted obiektu.

# Zadanie kończy się twardym błędem ObjectDoesNotExist.

# Jak to zapewnić?
# Używając metody transaction.on_commit(). Pozwala ona zarejestrować funkcję (np. wywołanie zadania Celery), 
# która zostanie uruchomiona dopiero po pomyślnym zakończeniu i zapisaniu transakcji w bazie.