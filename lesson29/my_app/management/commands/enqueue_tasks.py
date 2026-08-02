from django.core.management.base import BaseCommand
import random
# Importuję moje zadanie mnożenia z pliku tasks.py
from my_app.tasks import multiply 

class Command(BaseCommand):
    # Dodaję krótki opis komendy (wyświetli się przy wpisaniu python manage.py help)
    help = 'Dodaje 50 losowych zadań mnożenia do kolejki Celery'

    def handle(self, *args, **kwargs):
        self.stdout.write("Rozpoczynam dodawanie 50 zadań do kolejki...")
        
        # Tworzę pętlę, która wykona się 50 razy
        for i in range(50):
            # Losuję dwie liczby całkowite z przedziału od 1 do 100
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            
            # Wysyłam zadanie do kolejki za pomocą .delay()
            multiply.delay(a, b)
            
        # Drukuję w konsoli komunikat o sukcesie (na zielono!)
        self.stdout.write(self.style.SUCCESS('Sukces: Pomyślnie dodano 50 zadań do Celery!'))