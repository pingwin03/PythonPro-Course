# Zadanie 8 – Prosta symulacja
# Napisz zadanie, które symuluje przetwarzanie wideo przez 15 sekund (time.sleep(15)).
# Widok, który je wywołuje, powinien natychmiast zwrócić komunikat "Przetwarzanie wideo
# rozpoczęte!".


# Definicja zadania (my_app/tasks.py)
# Do symulacji opóźnienia wykorzystam wbudowaną bibliotekę time


from celery import shared_task
import time  # <--- Importuję bibliotekę time na górze pliku

# ... Moje poprzednie zadania ...

@shared_task
def process_video():
    print("Rozpoczynam przetwarzanie wideo...")
    
    # Symuluję ciężką pracę, zatrzymując działanie zadania na 15 sekund
    time.sleep(15)
    
    print("Sukces: Przetwarzanie wideo zakończone!")
    return True


# Widok wywołujący (my_app/views.py)

from django.http import HttpResponse
# Dodaję process_video do importów
from .tasks import hello_world, multiply, log_timestamp, count_users, update_user_last_login, process_video

# ... Moje poprzednie widoki ...

def process_video_view(request):
    # Wywołuję moje zadanie w tle używając .delay()
    process_video.delay()
    
    # Przeglądarka nie czeka 15 sekund! Od razu zwracam komunikat do użytkownika
    return HttpResponse("Przetwarzanie wideo rozpoczęte!")

# Ścieżka URL (my_project/urls.py)

from django.urls import path
from my_app import views

urlpatterns = [
    # ... moje poprzednie ścieżki ...
    path('process-video/', views.process_video_view, name='process_video'),
]



# test:
#     http://127.0.0.1:8000/process-video/
    
    
# Przeglądarka natychmiast pokaże napis "Przetwarzanie wideo rozpoczęte!". Strona nie będzie się "kręcić" i ładować przez 15 sekund.

# W oknie terminala workera zobaczę napis "Rozpoczynam przetwarzanie wideo...", a dopiero po 15 sekundach pojawi się napis informujący o sukcesie.