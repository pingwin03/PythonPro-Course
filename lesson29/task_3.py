# Zadanie 3 – Zapis do pliku
# Stwórz zadanie log_timestamp(), które zapisuje aktualną datę i godzinę do pliku log.txt.


# my_app/tasks.py


import datetime
from celery import shared_task


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


# my_app/views.py


from django.http import HttpResponse

from .tasks import hello_world, multiply, log_timestamp 

# ...  poprzednie widoki ...

def log_view(request):
    # Wywołuję zadanie asynchronicznie, przekazując je do Celery
    log_timestamp.delay()
    
    return HttpResponse("Polecenie zapisu do pliku zostało wysłane do Celery! Sprawdź folder projektu.")


# my_project/urls.py


from django.urls import path
from my_app import views

urlpatterns = [
    # ... poprzednie ścieżki ...
    path('log/', views.log_view, name='log_timestamp'),
]


celery -A my_project worker -l info -P solo.
http://127.0.0.1:8000/log/