# Zadanie 4 – Pierwsze zadanie z harmonogramem
# Użyj Celery Beat, aby uruchamiać zadanie log_timestamp() z poprzedniego ćwiczenia co
# 10 sekund.


# Konfiguracja harmonogramu (my_project/settings.py)

# Ustawienia dla Celery Beat
CELERY_BEAT_SCHEDULE = {
    'zapisuj-czas-co-10-sekund': {
        'task': 'my_app.tasks.log_timestamp',  # ścieżka do Twojego zadania
        'schedule': 10.0,                      # wykonuj co 10 sekund
    },
}


# 1. Pierwsze okno: Serwer Django (python manage.py runserver).

# 2. Drugie okno: Worker Celery (celery -A my_project worker -l info -P solo – 
# upewnij się, że zrestartowałeś workera, żeby załadował nowe ustawienia z settings.py!).

# 3. Trzecie okno (nowe): Otwórz nowy wiersz poleceń, przejdź do głównego 
# folderu projektu (tam, gdzie masz manage.py) i uruchom proces Beat komendą:
#     celery -A my_project beat -l info
    
#     Równo co 10 sekund Beat wyśle sygnał do kolejki.