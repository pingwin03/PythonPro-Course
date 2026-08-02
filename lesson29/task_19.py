# Zadanie 19 – Instalacja i eksploracja Flower
# Zainstaluj i uruchom Flower dla swojego projektu. Przejrzyj dostępne zakładki: dashboard,
# tasks, workers. Spróbuj wywołać zadanie z poziomu interfejsu Flower.

pip install flower

# Uruchomienie interfejsu:
    
# 1. Serwer Django (python manage.py runserver)

# 2. Przynajmniej jednego Workera Celery (: celery -A my_project worker -l info -P solo)

# Teraz otwieram kolejny, nowy terminal, aktywuje venv i wpisuje polecenie uruchamiające Flower:
celery -A my_project flower
    
# Eksploracja zakładek:
#     Domyślnie Flower uruchamia się na porcie 5555. Wchodzę pod adres: [http://127.0.0.1:5555]
    
# Dashboard: To główny pulpit. Widzisz tu podłączone workery, ich status (Online/Offline) 
# oraz liczbę zadań, które aktualnie przetwarzają


# Tasks (Zadania): To najważniejsza zakładka. Znajdziesz tu pełną historię wykonanych 
# (oraz działających w tle) zadań. Zobaczysz ich unikalne UUID, argumenty, które do nich trafiły, 
# czas wykonania i przede wszystkim status (SUCCESS, FAILURE, RETRY)


# Workers: Pokazuje szczegółowe informacje o Twoich procesach roboczych. 
# Jeśli klikniesz w nazwę workera, zobaczysz, jakie konkretnie ma skonfigurowane kolejki i limity

# Wywołanie zadania z poziomu interfejsu Flower
# W interfejsie Flower przechodze  do zakładki Workers i klikam w nazwę swojego aktywnego workera

# Przechodzę do podzakładki Tasks uruchamiam zadanie
# zakładki Tasks na górnym pasku Flower – widzę swoje wywołane przed sekundą zadanie ze statusem SUCCESS!