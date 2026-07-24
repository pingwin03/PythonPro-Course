# Zadanie 10 – Dodaj paginację do listy notatek
# W aplikacji "Notatnik" z zadania 6, zaimplementuj paginację na stronie z listą wszystkich
# notatek. Ustaw, aby na jednej stronie wyświetlały się maksymalnie 3 notatki. Dodaj w
# szablonie linki "następna" i "poprzednia".


# do - myapp/views.py    note_list_view

from django.core.paginator import Paginator

def note_list_view(request):
    # 1. Pobieramy wszystkie notatki i sortujemy je od najnowszych
    note_list = Note.objects.all().order_by('-id')
    
    # 2. Tworzymy obiekt Paginatora i mówimy mu: "3 notatki na jedną stronę"
    paginator = Paginator(note_list, 3)
    
    # 3. Sprawdzamy, na której stronie aktualnie jest użytkownik (z adresu np. ?page=2)
    page_number = request.GET.get('page')
    
    # 4. Pobieramy notatki tylko dla wybranej strony
    page_obj = paginator.get_page(page_number)
    
    # 5. Zamiast 'notes', do szablonu przekazujemy nasz nowy obiekt 'page_obj'
    return render(request, 'myapp/note_list.html', {'page_obj': page_obj})


# do - myapp/templates/myapp/note_list.html

{% extends "myapp/base.html" %}

{% block title %}Lista notatek{% endblock %}

{% block content %}
    <h1>Wszystkie notatki</h1>
    
    <!-- Zwróć uwagę, że iterujemy teraz po 'page_obj' -->
    <ul>
        {% for note in page_obj %}
            <!-- Zakładam, że masz tam linkowanie z poprzednich zadań, np. po ID -->
            <li>{{ note.title }}</li> 
        {% endfor %}
    </ul>

    <!-- Sekcja nawigacji paginacji -->
    <div style="margin-top: 20px;">
        <!-- Sprawdzamy, czy istnieje poprzednia strona -->
        {% if page_obj.has_previous %}
            <a href="?page={{ page_obj.previous_page_number }}">Poprzednia</a>
        {% endif %}

        <!-- Informacja o aktualnej stronie -->
        <span style="margin: 0 10px;">
            Strona {{ page_obj.number }} z {{ page_obj.paginator.num_pages }}.
        </span>

        <!-- Sprawdzamy, czy istnieje następna strona -->
        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}">Następna</a>
        {% endif %}
    </div>
{% endblock %}

# generuje to testów notatki
python manage.py shell
from myapp.models import Note

for i in range(1, 11):
    Note.objects.create(
        title=f"Testowa notatka {i}",
        content=f"To jest treść automatycznie wygenerowanej notatki numer {i}."
    )

print("Gotowe! 10 nowych notatek zostało dodanych do bazy.")

python manage.py runserver


http://127.0.0.1:8000/notes/