# Zadanie 9 – Masowe tworzenie zadań
# Napisz własną komendę manage.py (np. enqueue_tasks), która w pętli tworzy i dodaje do
# kolejki 50 zadań multiply z losowymi argumentami.


Kod własnej komendy (my_app/management/commands/enqueue_tasks.py
                     
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
        
#         test:
# python manage.py enqueue_tasks

# W terminalu, w którym wpisałeś komendę, od razu pojawi się informacja o dodaniu 50 zadań
# w workera Celery. widać "ścianę tekstu" – worker będzie błyskawicznie odbierał i wykonywał 
# 50 obliczeń matematycznych, wyświetlając ich wyniki jedno po drugim!