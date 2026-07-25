# cars/models.py
from django.db import models

# Tworzę model Dealera, który będzie mi potrzebny do realizacji Zadania 10
class Dealer(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        # Zwracam nazwę dealera jako reprezentację tekstową obiektu
        return self.name

# Tworzę główny model Car zgodnie z wytycznymi z polecenia
class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo = models.ImageField(upload_to='cars_photos/')
    owner_website = models.URLField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    
    # Dodaję klucz obcy do Dealera w ramach Zadania 10.
    # Ustawiam null=True i blank=True, by dealer nie był obowiązkowy dla starszych wpisów.
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='cars', null=True, blank=True)

    def __str__(self):
        # Definiuję czytelną nazwę w panelu admina na wypadek braku specjalnych konfiguracji
        return f"{self.brand} {self.model}"