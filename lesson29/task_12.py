# Zadanie 12 – Czyszczenie bazy danych
# Napisz zadanie, które usuwa z bazy wszystkie obiekty modelu LogEntry (musisz go
# najpierw stworzyć) starsze niż 90 dni. Uruchom to zadanie za pomocą Celery Beat raz



# Tworzenie modelu LogEntry (my_app/models.py)
# Najpierw potrzebuję miejsca, w którym będę trzymał logi. Dodaję prosty model z datą utworzenia.

# Dodaję to na końcu pliku my_app/models.py

class LogEntry(models.Model):
    # Tworzę proste pole tekstowe na treść loga
    message = models.CharField(max_length=255)
    
    # auto_now_add=True sprawia, że Django samo wstawi obecną datę przy tworzeniu obiektu
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log z {self.created_at.strftime('%Y-%m-%d')}: {self.message}"
    
    
#  python manage.py makemigrations
# python manage.py migrate   


# Pisanie zadania czyszczącego (my_app/tasks.py)
# Teraz muszę napisać logikę, która obliczy datę sprzed 90 dni i usunie wszystko,
# co jest od niej starsze. Użyję do tego wbudowanych narzędzi z biblioteki datetime
# oraz mechanizmów czasu Django.


from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import LogEntry # <--- Importuję mój nowy model

# ... moje poprzednie zadania ...

@shared_task
def cleanup_old_logs():
    print("Rozpoczynam czyszczenie starych logów...")
    
    # Obliczam graniczną datę (obecny czas minus 90 dni)
    threshold_date = timezone.now() - timedelta(days=90)
    
    # Filtruję obiekty, w których 'created_at' jest mniejsze (starsze) niż threshold_date
    # Metoda delete() zwraca krotkę, z której interesuje mnie tylko pierwsza wartość (ilość usuniętych)
    deleted_count, _ = LogEntry.objects.filter(created_at__lt=threshold_date).delete()
    
    print(f"Zakończono sprzątanie. Usunięto {deleted_count} wpisów.")
    return deleted_count


# Konfiguracja Celery Beat (my_project/celery.py)

from celery.schedules import crontab

# ... reszta pliku celery.py ...

app.conf.beat_schedule = {
    # ... ewentualne inne zaplanowane zadania z lekcji 1-6 ...
    
    # Definiuję moje nowe cykliczne zadanie
    'cleanup-logs-daily': {
        'task': 'my_app.tasks.cleanup_old_logs',
        
        # Ustawiam harmonogram na codziennie o północy (00:00)
        'schedule': crontab(minute=0, hour=0), 
    },
}

# test:
#     Worker: celery -A my_project worker -l info -P solo
#     Beat: celery -A my_project beat -l info (Ważne! To ten proces czyta nasz beat_schedule i wyzwala zadania o konkretnej porze)
    
# pojawiło się cleanup-logs-daily, to znaczy, że zadanie zostało poprawnie zaplanowane i odpali się punktualnie o północy    