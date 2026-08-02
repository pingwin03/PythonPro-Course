# Zadanie 17 – Łańcuchy zadań (Chains)
# Zapoznaj się z dokumentacją Celery na temat chains. Stwórz łańcuch trzech zadań:
# pierwsze generuje losową liczbę, drugie mnoży ją przez 10, a trzecie zapisuje wynik do
# pliku. Wywołaj cały łańcuch jednym poleceniem z widoku Django.





# Trzy małe zadania w my_app/tasks.py



import random
import os
from django.conf import settings
from celery import shared_task

# ... moje poprzednie zadania ...

@shared_task
def generate_random_number():
    # Krok 1: Losuję liczbę
    number = random.randint(1, 100)
    print(f"\n[Łańcuch - Krok 1] Wylosowałem: {number}")
    
    # Zwracam ją - Celery automatycznie przekaże ją do kolejnego zadania!
    return number

@shared_task
def multiply_by_10(number):
    # Krok 2: Przyjmuję 'number' z poprzedniego zadania i mnożę
    result = number * 10
    print(f"[Łańcuch - Krok 2] Pomnożyłem {number} x 10. Wynik to: {result}")
    
    # Zwracam wynik - Celery wrzuci go do kroku nr 3!
    return result

@shared_task
def save_result_to_file(final_result):
    # Krok 3: Przyjmuję wynik i zapisuję go na dysku
    # Używam MEDIA_ROOT, żeby zapisać to w E:\PythonPro-Course\homework\lesson29\media\
    file_path = os.path.join(settings.MEDIA_ROOT, 'chain_results.txt')
    
    # Otwieram plik w trybie 'a' (append), żeby dopisywać kolejne wyniki na końcu
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f"Wynik dzialania lancucha: {final_result}\n")
        
    print(f"[Łańcuch - Krok 3] Zapisano {final_result} w pliku {file_path}")
    return "Łańcuch zakończony sukcesem!"


# Widok wyzwalający w my_app/views.py


from django.http import JsonResponse
from celery import chain
from .tasks import generate_random_number, multiply_by_10, save_result_to_file

# ... moje poprzednie widoki ...

def start_chain_view(request):
    # Buduję mój łańcuch używając sygnatur .s()
    # Zauważ, że w .s() do zadań 2 i 3 nie wpisuję żadnych argumentów - Celery samo "wepnie" tam wyniki z poprzednich kroków.
    my_workflow = chain(
        generate_random_number.s(),
        multiply_by_10.s(),
        save_result_to_file.s()
    )
    
    # Uruchamiam cały zestaw jednym poleceniem (można też użyć my_workflow.apply_async())
    my_workflow()

    # Odpowiadam użytkownikowi, żeby wiedział, że proces ruszył
    return JsonResponse({
        'status': 'Sukces',
        'message': 'Łańcuch zadań został wystrzelony! Zobacz konsolę Workera i plik chain_results.txt w folderze media.'
    })
    
    
# Ścieżka URL w my_project/urls.py

path('test-chain/', views.start_chain_view, name='start_chain'),


# Test:
# celery -A my_project worker -l info -P solo

# http://127.0.0.1:8000/test-chain/
# plik chain_results.txt pojawił się obok moich obrazków i raportów CSV w folderze media.

