# Zadanie 2 – Zadanie z argumentami
# Zadania-wyzwania (challenge)
# Napisz zadanie multiply(a, b), które przyjmuje dwie liczby i zwraca ich iloczyn. W widoku
# stwórz prosty formularz HTML z dwoma polami, z których pobierzesz liczby i przekażesz je
# do zadania Celery.


# my_app/tasks.py

from celery import shared_task

# ... poprzednie zadania ...

@shared_task
def multiply(a, b):
    # Rzutuję argumenty na typ zmiennoprzecinkowy (float), na wypadek gdyby dotarły jako tekst
    wynik = float(a) * float(b)
    
    # Drukuję wynik w konsoli workera, abym mógł łatwo zweryfikować działanie
    print(f"Obliczyłem iloczyn: {a} * {b} = {wynik}")
    
    # Zwracam wynik zgodnie z poleceniem



# my_app/views.py


from django.http import HttpResponse
from .tasks import multiply

def multiply_view(request):
    # Pobieram liczby 'a' i 'b' przekazane przez formularz w adresie URL[cite: 1]
    a = request.GET.get('a')
    b = request.GET.get('b')
    
    # Sprawdzam, czy obie liczby zostały podane (czyli czy formularz został wysłany)
    if a is not None and b is not None:
        # Wywołuję moje zadanie w tle, przekazując pobrane liczby jako argumenty[cite: 1]
        multiply.delay(a, b)
        
        # Zwracam natychmiastową odpowiedź do przeglądarki
        return HttpResponse(f"Wysłałem do Celery polecenie pomnożenia {a} przez {b}! Sprawdź konsolę workera.")

    # Jeśli użytkownik dopiero wszedł na stronę, przygotowuję i zwracam mu prosty formularz HTML[cite: 1]
    html_form = """
    <h2>Zadanie 2: Mnożenie w Celery</h2>
    <form method="get">
        <label>Liczba A: <input type="number" step="any" name="a" required></label><br><br>
        <label>Liczba B: <input type="number" step="any" name="b" required></label><br><br>
        <button type="submit">Pomnóż asynchronicznie</button>
    </form>
    """
    return HttpResponse(html_form)


# my_project/urls.py


from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.trigger_hello_world, name='hello_world'),
    # Dodaję nową ścieżkę dla formularza mnożenia
    path('multiply/', views.multiply_view, name='multiply'),
]
# term. 1 - celery -A my_project worker -l info -P solo
# term. 2 - python manage.py runserver
http://127.0.0.1:8000/multiply/