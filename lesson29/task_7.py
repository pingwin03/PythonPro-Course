# Zadanie 7 – Przekazywanie ID obiektu
# Stwórz zadanie update_user_last_login(user_id), które przyjmuje ID użytkownika, znajduje
# go w bazie i aktualizuje jego pole last_login na aktualny czas.Tip
# Do zadań Celery zawsze przekazuj proste typy danych (jak ID), a nie całe obiekty
# Django. Obiekt w momencie wykonania zadania może już być inny niż w momencie
# jego wywołania


Definicja zadania (my_app/tasks.py)


from celery import shared_task
from django.contrib.auth.models import User 
from django.utils import timezone  # <--- Dodaje ten import na górze pliku

#

@shared_task
def update_user_last_login(user_id):
    try:
        # 1. Szukam użytkownika o podanym ID w bazie danych
        user = User.objects.get(id=user_id)
        
        # 2. Aktualizuje pole last_login na dokładny, obecny czas
        user.last_login = timezone.now()
        
        # 3. Zapisuje zmiany w bazie
        user.save()
        
        print(f"Sukces: Zaktualizowano czas logowania dla użytkownika {user.username} (ID: {user_id})")
        return True
        
    except User.DoesNotExist:
        # Obsługa błędu na wypadek, gdyby podano ID, którego nie ma w bazie
        print(f"Błąd: Użytkownik o ID {user_id} nie istnieje w bazie danych.")
        return False
    


# Widok testowy (my_app/views.py)

    
from django.http import HttpResponse
# Pamiętam o dodaniu update_user_last_login do importów!
from .tasks import hello_world, multiply, log_timestamp, count_users, update_user_last_login

# ... Moje poprzednie widoki ...

def update_login_view(request):
    # Wywołuję zadanie i przekazuję mu argument (np. ID = 1)
    # Zamiast w nawiasach zwykłych, argument podaję w nawiasach od .delay()
    update_user_last_login.delay(1)
    
    return HttpResponse("Wysłano zadanie aktualizacji czasu logowania dla użytkownika ID=1!")


# Ścieżka URL (my_project/urls.py)

from django.urls import path
from my_app import views

urlpatterns = [
    # ... moje poprzednie ścieżki ...
    path('update-login/', views.update_login_view, name='update_login'),
]

# test:
#     http://127.0.0.1:8000/update-login/
# konsola Workera:  Błąd, bo nie mam jeszcze żadnego użytkownika o ID 1).
# jak by był to Sukces: Zaktualizowano czas...