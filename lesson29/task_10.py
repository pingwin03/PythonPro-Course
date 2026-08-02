# Zadanie 10 – Powiadomienie mailowe
# Rozbuduj zadanie z symulacją wysyłki maila. Stwórz prosty model EmailNotification z
# polami recipient_email, subject, body i sent_at (nullable). Zadanie Celery powinno przyjąć
# ID obiektu tego modelu, wysłać "maila" (czyli zasymulować opóźnienie) i po zakończeniu
# zaktualizować pole sent_at na aktualny czas.


# Definicja modelu (my_app/models.py)

from django.db import models

class EmailNotification(models.Model):
    recipient_email = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    # Ustawiam null=True i blank=True, aby pole mogło być na początku puste
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        # Zwracam czytelny opis obiektu, co przyda się m.in. w panelu admina
        return f"Mail do: {self.recipient_email} - {self.subject}"
    
    
# python manage.py makemigrations
# python manage.py migrate    



# Definicja zadania (my_app/tasks.py)


from celery import shared_task
from django.utils import timezone
import time
from .models import EmailNotification  # <--- Importuję mój nowy model

# ... Moje poprzednie zadania ...

@shared_task
def send_email_notification(notification_id):
    try:
        # 1. Pobieram powiadomienie z bazy na podstawie otrzymanego ID
        notification = EmailNotification.objects.get(id=notification_id)
        
        print(f"Rozpoczynam wysyłanie maila do {notification.recipient_email}...")
        
        # 2. Symuluję proces wysyłania maila (np. 5 sekund opóźnienia)
        time.sleep(5)
        
        # 3. Aktualizuję pole sent_at na dokładny, obecny czas
        notification.sent_at = timezone.now()
        
        # 4. Zapisuję zmiany w bazie danych
        notification.save()
        
        print(f"Sukces: Mail wysłany! Zaktualizowano czas wysyłki dla ID {notification_id}.")
        return True
        
    except EmailNotification.DoesNotExist:
        # Obsługuję sytuację, w której powiadomienie o tym ID nie istnieje w bazie
        print(f"Błąd: Powiadomienie o ID {notification_id} nie istnieje.")
        return False
    
    
#  Widok testowy (my_app/views.py)   

from django.http import HttpResponse
from .models import EmailNotification
# Dodaję nowe zadanie do importów
from .tasks import hello_world, multiply, log_timestamp, count_users, update_user_last_login, process_video, send_email_notification

# ... Moje poprzednie widoki ...

def trigger_email_view(request):
    # 1. Tworzę nowy wpis w bazie danych (data wysłania pozostaje pusta)
    notification = EmailNotification.objects.create(
        recipient_email="test@example.com",
        subject="Witaj w systemie!",
        body="To jest testowa wiadomość."
    )
    
    # 2. Przekazuję ID nowo utworzonego obiektu do zadania w tle
    send_email_notification.delay(notification.id)
    
    # Od razu zwracam odpowiedź do użytkownika
    return HttpResponse(f"Zadanie wysłania maila zostało dodane do kolejki! ID powiadomienia: {notification.id}")


# Ścieżka URL (my_project/urls.py)

from django.urls import path
from my_app import views

urlpatterns = [
    # ... moje poprzednie ścieżki ...
    path('send-email/', views.trigger_email_view, name='send_email'),
]

# test:
# (http://127.0.0.1:8000/send-email/). Zobaczysz komunikat o utworzeniu zadania i przyznanym ID obiektu.
# w terminalu Workera widac info o wysyłaniu maila i sukces