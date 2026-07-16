# Zadanie 6

from django.db import models

class Ogloszenie(models.Model):
    tytul = models.CharField(max_length=100) # Tekst, max 100 znaków
    opis = models.TextField()                # Dłuższy tekst
    # Liczba dziesiętna: max 8 cyfr łącznie, w tym dokładnie 2 po przecinku
    cena = models.DecimalField(max_digits=8, decimal_places=2) 
    # Data i czas, ustawiane automatycznie podczas tworzenia rekordu
    data_dodania = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.tytul  # Wyświetli tytuł ogłoszenia w panelu