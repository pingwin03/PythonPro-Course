# Zadanie 13 – Web scraping w tle
# Stwórz zadanie, które używa biblioteki requests i BeautifulSoup4 do pobrania tytułu strony
# https://example.com i zapisania go w bazie danych. Zadanie to ma być uruchamiane co
# godzinę


pip install requests beautifulsoup4


# Model bazy danych (my_app/models.py)

# Dodaję nowy model na końcu pliku my_app/models.py

class ScrapedWebsite(models.Model):
    # Tworzę pole tekstowe na tytuł strony
    title = models.CharField(max_length=255)
    
    # Automatycznie zapisuję dokładną datę i godzinę pobrania danych
    scraped_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} (pobrano: {self.scraped_at.strftime('%Y-%m-%d %H:%M')})"
    
    
    
    
python manage.py makemigrations
python manage.py migrate




    # Logika web scrapingu (my_app/tasks.py)
    
import requests
from bs4 import BeautifulSoup
from celery import shared_task
from .models import ScrapedWebsite # <--- Importuję mój nowy model

# ... moje poprzednie zadania ...

@shared_task
def scrape_example_com():
    print("Rozpoczynam pobieranie tytułu ze strony example.com...")
    
    url = 'https://example.com'
    
    # Pobieram zawartość strony używając biblioteki requests
    response = requests.get(url)
    
    # Upewniam się, że żądanie zakończyło się sukcesem (status 200)
    response.raise_for_status()
    
    # Parsuję kod HTML pobranej strony za pomocą BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Wyciągam zawartość znacznika <title>. Jeśli go nie ma, ustawiam wartość domyślną.
    page_title = soup.title.string if soup.title else "Brak tytułu"
    
    # Zapisuję wyciągnięty tytuł do mojej bazy danych
    ScrapedWebsite.objects.create(title=page_title)
    
    print(f"Sukces! Zapisano tytuł: {page_title}")
    
    return page_title



# Harmonogram Celery Beat (my_project/celery.py)
from celery.schedules import crontab

# ... reszta pliku celery.py ...

app.conf.beat_schedule = {
    # ... moje poprzednie zaplanowane zadania (np. cleanup-logs-daily) ...
    
    # Dodaję nowe zadanie scrapowania
    'scrape-example-hourly': {
        'task': 'my_app.tasks.scrape_example_com',
        
        # Ustawiam harmonogram: uruchamiaj co godzinę (o każdej zerowej minucie danej godziny)
        'schedule': crontab(minute=0), 
    },
}

# Wyłącz i włącz Workera: celery -A my_project worker -l info -P solo
# Wyłącz i włącz Beat'a: celery -A my_project beat -l info


# Zadanie odpali się samo o najbliższej pełnej godzinie. 
# Jeśli chcemy przetestować je natychmiast i nie czekać, możemy wywołać z 
# głównego terminala naszą konsolę Django (python manage.py shell) i odpalić zadanie ręcznie:

from my_app.tasks import scrape_example_com
scrape_example_com.delay()