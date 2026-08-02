# Zadanie 1 – Pierwsze zadanie
# Stwórz w pliku tasks.py proste zadanie o nazwie hello_world, które po prostu drukuje w
# konsoli workera napis "Hello from Celery!". Stwórz widok Django, który po wejściu na
# odpowiedni URL wywoła to zadanie.

my_app/tasks.py
from celery import shared_task

@shared_task
def hello_world():
    # Drukuję w konsoli mojego workera wymagany napis "Hello from Celery!"
    print("Hello from Celery!")
    
    
    
my_app/views.py    
 from django.http import HttpResponse
from .tasks import hello_world

def trigger_hello_world(request):
    # Wywołuję moje zadanie asynchronicznie w tle za pomocą metody delay()
    hello_world.delay()
    
    # Natychmiast zwracam odpowiedź HTTP dla przeglądarki, nie czekając na workera
    return HttpResponse("Zadanie hello_world zostało poprawnie wysłane do kolejki Celery!")   



my_project/urls.py
from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Ustawiam ścieżkę 'hello/', po wejściu na którą wywołam mój widok trigger_hello_world[cite: 1]
    path('hello/', views.trigger_hello_world, name='hello_world'),
]
# term. 1 - celery -A my_project worker -l info
# term. 2 - python manage.py runserver

http://127.0.0.1:8000/hello/