# Zadanie 6 – Wyszukiwarka Postów
# Stwórz prostą wyszukiwarkę. Dodaj formularz na stronie głównej, który wysyła zapytanie
# GET z frazą szukaną. Stwórz widok, który odbierze tę frazę i odfiltruje posty, których tytuł
# lub treść zawiera daną frazę (__icontains będzie tu bardzo pomocne). (challenge)

# do - blog/views.py

from django.shortcuts import render, get_object_or_404
from django.db.models import Q  # Importujemy obiekt Q do zapytań "LUB"
from .models import Post, Category

# Widok kategorii z Zadania 2 zostaje bez zmian...
def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category)
    context = {'category': category, 'posts': posts}
    return render(request, 'blog/category_posts.html', context)

# Zaktualizowany widok dla Zadania 6
def home(request):
    # Pobieram frazę z parametru 'q' (request.GET to słownik z parametrami URL)
    query = request.GET.get('q')
    
    if query:
        # Jeśli użytkownik czegoś szuka, filtrujemy tytuł LUB treść
        # Używamy __icontains, aby ignorować wielkość liter
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).order_by('-publication_date')
    else:
        # Jeśli nie ma zapytania, pokazujemy 5 najnowszych (jak w Zadaniu 3)
        posts = Post.objects.order_by('-publication_date')[:5]
    
    context = {
        'posts': posts,
        'query': query, # Przekazuje frazę do szablonu, by ją tam wyświetlić
    }
    return render(request, 'blog/home.html', context)


# Dodanie wyszukiwarki do szablonu (blog/templates/blog/home.html)

<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Strona Główna Bloga</title>
</head>
<body>
    <h1>Blog</h1>

    <!-- FORMULARZ WYSZUKIWARKI -->
    <form method="GET" action="">
        <input type="text" name="q" placeholder="Szukaj postów..." value="{{ query|default_if_none:'' }}">
        <button type="submit">Szukaj</button>
    </form>
    
    <hr>

    <!-- Nagłówek dynamiczny: zależy czy jesteśmy w trakcie szukania -->
    {% if query %}
        <h2>Wyniki wyszukiwania dla: "{{ query }}"</h2>
    {% else %}
        <h2>Ostatnie posty na blogu</h2>
    {% endif %}
    
    {% if posts %}
        <ul>
            {% for post in posts %}
                <li>
                    <strong>{{ post.title }}</strong> 
                    <br>
                    <small>Data: {{ post.publication_date|date:"d.m.Y H:i" }} | Autor: {{ post.author.name }}</small>
                </li>
            {% endfor %}
        </ul>
    {% else %}
        <p>Brak postów pasujących do podanych kryteriów.</p>
    {% endif %}
</body>
</html>



http://127.0.0.1:8000/