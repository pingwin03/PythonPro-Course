# Zadanie 6 – Harmonogram z crontab
# Skonfiguruj Celery Beat tak, aby zadanie count_users() uruchamiało się codziennie o
# godzinie 23:00


Konfiguracja crontab (my_project/settings.py)

# Import funkcji crontab (dodaj to najlepiej nad słownikiem)
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    # Możesz zostawić to zadanie, lub je zakomentować, by nie śmieciło logów
    # 'zapisuj-czas-co-10-sekund': {
    #     'task': 'my_app.tasks.log_timestamp',
    #     'schedule': 10.0,
    # },
    
    # Nowe zadanie: uruchamiaj o 23:00 każdego dnia
    'policz-uzytkownikow-codziennie-o-23': {
        'task': 'my_app.tasks.count_users',  # Ścieżka do zadania z poprzedniego kroku
        'schedule': crontab(hour=23, minute=0),
    },
}

# test:
# celery -A my_project beat -l info
# Aby szybko przetestować, czy harmonogram faktycznie przekazuje zadanie do workera, zmieniam na chwilę w settings.py konfigurację na:
# 'schedule': crontab(minute='*'), (co oznacza: uruchamiaj zadanie w każdej nowej minucie).