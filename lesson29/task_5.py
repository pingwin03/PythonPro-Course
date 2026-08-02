
# Zadanie 5 – Zmiana w bazie danych
# Stwórz zadanie count_users(), które liczy wszystkich użytkowników w bazie danych
# (User.objects.count()) i drukuje wynik w konsoli workera.

# Definicja zadania (my_app/tasks.py)

from celery import shared_task
# Importuję wbudowany model użytkownika Django
from django.contrib.auth.models import User 



@shared_task
def count_users():
    # Pobieram liczbę wszystkich użytkowników z bazy danych
    liczba = User.objects.count()
    
    # Drukuję wynik w konsoli workera, tak jak w poleceniu
    print(f"Aktualna liczba użytkowników w bazie: {liczba}")
    
    return liczba


# Widok do uruchomienia zadania (my_app/views.py)

from django.http import HttpResponse
# Pamiętaj, aby dodać count_users do importów z .tasks!
from .tasks import hello_world, multiply, log_timestamp, count_users 

# ... Twoje poprzednie widoki ...

def count_users_view(request):
    # Wysyłam zadanie do Celery
    count_users.delay()
    
    return HttpResponse("Zadanie zliczania użytkowników zostało wysłane. Sprawdź terminal workera!")

# Podłączenie adresu URL (my_project/urls.py)

from django.urls import path
from my_app import views

urlpatterns = [
    # ... poprzednie ścieżki ...
    path('count-users/', views.count_users_view, name='count_users'),
]


# celery -A my_project worker -l info -P solo
# http://127.0.0.1:8000/count-users/

# log z informacją o liczbie użytkowników