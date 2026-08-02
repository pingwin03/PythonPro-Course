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
    
class LogEntry(models.Model):
    # Tworzę proste pole tekstowe na treść loga
    message = models.CharField(max_length=255)
    
    # auto_now_add=True sprawia, że Django samo wstawi obecną datę przy tworzeniu obiektu
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log z {self.created_at.strftime('%Y-%m-%d')}: {self.message}"    
    
class ScrapedWebsite(models.Model):
    # Tworzę pole tekstowe na tytuł strony
    title = models.CharField(max_length=255)
    
    # Automatycznie zapisuję dokładną datę i godzinę pobrania danych
    scraped_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} (pobrano: {self.scraped_at.strftime('%Y-%m-%d %H:%M')})"
    
    
class UploadedImage(models.Model):
    # Przesyłane pliki będą lądować w E:\PythonPro-Course\homework\lesson29\media\images\
    image = models.ImageField(upload_to='images/')
    
    # Pole na nasz wynik analizy, domyślnie puste (bo na początku obraz jeszcze nie jest przetworzony)
    classification_result = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Obraz {self.id}"