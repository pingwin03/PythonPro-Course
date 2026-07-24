# Zadanie 1 – Nowy model
# Stwórz w swojej aplikacji nowy model o nazwie Category z jednym polem name typu
# CharField. Następnie wygeneruj i wykonaj migracje, aby stworzyć odpowiednią tabelę w
# bazie danych


do - articles/models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    # Migracja w terminalu
    python manage.py makemigrations
python manage.py migrate