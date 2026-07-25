# Zadanie 8 – Normalizacja Postów (Tagi)
# Zaprojektuj i zaimplementuj system tagów. Stwórz model Tag z polem name. Post może
# mieć wiele tagów, a tag może być przypisany do wielu postów. Jakiego pola relacyjnego
# użyjesz w modelu Post? (podpowiedź: ManyToManyField). Pamiętaj o migracjach.


# Aktualizacja modeli (blog/models.py)
from django.db import models
from django.utils import timezone



class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    
    # NOWE POLE RELACYJNE
    # blank=True oznacza, że post może nie mieć żadnych tagów (nie są obowiązkowe)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title



# Migracja
python manage.py makemigrations
python manage.py migrate




# Aby móc łatwo dodawać i zarządzać tagami przez przeglądarkę, 
# dodaje ten model do panelu admina. Otwórz plik blog/admin.py

from django.contrib import admin
from .models import Post, Category, Author, Tag  # Importuje nowy model Tag

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Tag)  # Rejestruje Tag