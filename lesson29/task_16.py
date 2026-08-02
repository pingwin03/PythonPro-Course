# Zadanie 16 – [AI] Klasyfikacja obrazu w tle
# Stwórz model UploadedImage z polem ImageField oraz classification_result (CharField).
# Gdy użytkownik prześle obrazek, zapisz go i uruchom zadanie Celery, przekazując ID
# obrazka. Zadanie powinno użyć biblioteki Pillow do otwarcia obrazka i "sklasyfikowania" go
# (np. sprawdź, czy jest w skali szarości, czy kolorowy, jakie ma wymiary) i zapisać wynik w
# polu classification_result. To uproszczona wersja prawdziwego zadania AI.


pip install Pillow

# Tworzę model w my_app/models.py

from django.db import models

# ... moje poprzednie modele ...

class UploadedImage(models.Model):
    # Przesyłane pliki będą lądować w E:\PythonPro-Course\homework\lesson29\media\images\
    image = models.ImageField(upload_to='images/')
    
    # Pole na nasz wynik analizy, domyślnie puste (bo na początku obraz jeszcze nie jest przetworzony)
    classification_result = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Obraz {self.id}"
    
    
    
 python manage.py makemigrations
python manage.py migrate



#    Piszę zadanie Celery w my_app/tasks.py


from celery import shared_task
from .models import UploadedImage
from PIL import Image

# ... moje poprzednie zadania ...

@shared_task
def classify_image_task(image_id):
    # 1. Pobieram mój obraz z bazy danych na podstawie przekazanego ID
    try:
        img_obj = UploadedImage.objects.get(id=image_id)
    except UploadedImage.DoesNotExist:
        return "Błąd: Obraz nie istnieje w bazie."

    # 2. Otwieram fizyczny plik na moim dysku. 
    # img_obj.image.path zwraca pełną, fizyczną ścieżkę w systemie Windows
    try:
        with Image.open(img_obj.image.path) as img:
            width, height = img.size
            mode = img.mode  # Np. 'RGB' dla kolorowych, 'L' dla czarno-białych
            
            # Prosta "klasyfikacja"
            if mode in ['RGB', 'RGBA']:
                color_type = "Kolorowy"
            elif mode == 'L':
                color_type = "Skala szarości (czarno-biały)"
            else:
                color_type = f"Inny (tryb {mode})"
                
            # Formatuję mój wynik
            result = f"Rozmiar: {width}x{height}px, Kolor: {color_type}"
            
    except Exception as e:
        result = f"Błąd podczas analizy: {str(e)}"
        
    # 3. Zapisuję wynik w bazie danych
    img_obj.classification_result = result
    img_obj.save()
    
    # Zwracam też wynik tekstowy, żeby był widoczny w logach Workera
    return f"Zakończono analizę obrazu {image_id}: {result}"


# Przygotowuję widok w my_app/views.py


from django.shortcuts import render, redirect
from .models import UploadedImage
from .tasks import classify_image_task

# ... moje poprzednie widoki ...

def upload_image_view(request):
    if request.method == 'POST' and request.FILES.get('image'):
        # Tworzę nowy wpis w bazie i zapisuję obrazek na dysk
        new_img = UploadedImage.objects.create(
            image=request.FILES['image']
        )
        
        # Uruchamiam asynchronicznie moją analizę - przekazuję tylko ID!
        classify_image_task.delay(new_img.id)
        
        # Zabezpieczam przed podwójnym wysłaniem formularza przez odświeżenie (Redirect po POST)
        return redirect('upload_image')

    # Pobieram wszystkie obrazki, najnowsze na górze
    images = UploadedImage.objects.all().order_by('-id')
    return render(request, 'upload_image.html', {'images': images})


# Dodaję prosty szablon HTML
# my_app/templates/upload_image.html


<!DOCTYPE html>
<html>
<head>
    <title>Analiza AI w Celery</title>
</head>
<body style="font-family: sans-serif; padding: 20px;">
    <h2>Wgraj obrazek do analizy</h2>
    
    <!-- Pamiętam o enctype="multipart/form-data" przy przesyłaniu plików! -->
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        <input type="file" name="image" accept="image/*" required>
        <button type="submit">Wgraj i przeanalizuj</button>
    </form>

    <hr>
    <h3>Historia obrazków:</h3>
    <ul>
        {% for img in images %}
            <li style="margin-bottom: 10px;">
                <strong>Obraz #{{ img.id }}</strong> 
                (<a href="{{ img.image.url }}" target="_blank">podgląd</a>) <br>
                Wynik klasyfikacji: 
                {% if img.classification_result %}
                    <span style="color: green;">{{ img.classification_result }}</span>
                {% else %}
                    <span style="color: orange;">Oczekuje na wynik od Celery... (odśwież stronę za chwilę)</span>
                {% endif %}
            </li>
        {% empty %}
            <li>Brak obrazków.</li>
        {% endfor %}
    </ul>
</body>
</html>


# Na koniec ścieżka w my_project/urls.py

path('upload-image/', views.upload_image_view, name='upload_image'),



# Test:

# python manage.py runserver
# celery -A my_project worker -l info -P solo

# http://127.0.0.1:8000/upload-image/
# Wgrywam zdjęcie to restu
# NA konsoli wORKERA WIDZ E ZE ZADANIE ZOSTALO PODJĘTE
# A POOD ŚWIEŻENIU PORZEGLĄDARKI  POMARA ŃCZOWY NAPIS "OCZEKUJE" ZMIENIŁ SE NA ZIELONY WYNIK ANALIZY