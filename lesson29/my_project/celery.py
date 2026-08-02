
import os
from celery import Celery
from celery.schedules import crontab

# Ustawiam domyślną zmienną środowiskową, żeby Celery wiedziało, gdzie są moje ustawienia projektu
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')

# Tworzę instancję mojej aplikacji Celery
app = Celery('my_project')

# Wczytuję konfigurację z pliku settings.py. 
# Używam namespace='CELERY', więc wszystkie moje ustawienia w settings.py muszą zaczynać się od tego prefiksu
app.config_from_object('django.conf:settings', namespace='CELERY')

# Każe Celery automatycznie szukać zadań w plikach tasks.py we wszystkich moich aplikacjach
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    
    
app.conf.beat_schedule = {
    # Moje zadanie z lekcji 12 (Czyszczenie logów)
    'cleanup-logs-daily': {
        'task': 'my_app.tasks.cleanup_old_logs',
        'schedule': crontab(minute=0, hour=0),
    }, # <--- Pamiętam o przecinku oddzielającym zadania!

    # Moje zadanie z lekcji 13 (Web scraping)
    'scrape-example-hourly': {
        'task': 'my_app.tasks.scrape_example_com',
        'schedule': crontab(minute=0),
    },
} # <--- Ten nawias zamyka cały słownik konfiguracyjny!