# Zadanie 6 – Aplikacja "Notatnik"
# Stwórz prostą aplikację do robienia notatek.
# 1. Zdefiniuj model Note z polami title (CharField) i content (TextField).
# 2. Stwórz widok, który wyświetli listę wszystkich notatek.
# 3. Stwórz drugi widok, który wyświetli szczegóły pojedynczej notatki (użyj trasy
# dynamicznej /note/<int:note_id>/)



#do- myapp/models.py

from django.db import models

# Twój wcześniejszy model Product powinien tu być

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    
#  python manage.py makemigrations

# python manage.py migrate

do - myapp/views.py

from django.shortcuts import render, get_object_or_404
from .models import Product, Note # Pamiętaj o zaimportowaniu modelu Note!

# Widok 1: Lista wszystkich notatek
def note_list_view(request):
    notes = Note.objects.all()
    return render(request, 'myapp/note_list.html', {'notes': notes})

# Widok 2: Szczegóły pojedynczej notatki
def note_detail_view(request, note_id):
    # get_object_or_404 to bezpieczny sposób pobierania - wyrzuci błąd 404, jeśli notatka nie istnieje
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'myapp/note_detail.html', {'note': note})

# do - urls.py

from django.urls import path
# Upewnij się, że importujesz nowe widoki:
from myapp.views import info_view, product_list_view, note_list_view, note_detail_view

urlpatterns = [
    # ... twoje stare ścieżki ...
    path('notes/', note_list_view, name='note_list'),
    path('note/<int:note_id>/', note_detail_view, name='note_detail'),
]

# w - myapp/templates/myapp/  tworzę 2  pliki note_list.html , note_detail.html
from django.urls import path
# Upewnij się, że importujesz nowe widoki:
from myapp.views import info_view, product_list_view, note_list_view, note_detail_view

urlpatterns = [
    # ... twoje stare ścieżki ...
    path('notes/', note_list_view, name='note_list'),
    path('note/<int:note_id>/', note_detail_view, name='note_detail'),
]



{% extends "myapp/base.html" %}

{% block title %}Moje notatki{% endblock %}

{% block content %}
    <h1>Lista notatek</h1>
    <ul>
        {% for note in notes %}
            <li>
                <a href="/note/{{ note.id }}/">{{ note.title }}</a>
            </li>
        {% empty %}
            <li>Brak notatek.</li>
        {% endfor %}
    </ul>
{% endblock %}

# dodaje daner to testów:
    python manage.py shell
    from myapp.models import Note
Note.objects.create(title="Plan treningowy", content="3-dniowy trening siłowy na redukcję. Rozkład na poszczególne partie mięśniowe z uwzględnieniem docelowego deficytu kalorii.")
exit()

http://127.0.0.1:8000/notes/