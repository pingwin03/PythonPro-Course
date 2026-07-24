# Zadanie 10 – Prosty formularz wyszukiwania
# W szablonie listy artykułów (article_list.html) dodaj prosty formularz HTML (
# ...
# ) z jednym polem . W widoku article_list_view sprawdź, czy w
# żądaniu GET istnieje parametr q (request.GET.get('q')). Jeśli tak, przefiltruj artykuły, aby
# pokazać tylko te, których tytuł zawiera szukaną frazę.


# do - articles/views.py
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Category, Article



def article_list_view(request):
    # Najpierw pobieramy wszystkie opublikowane artykuły
    articles = Article.objects.filter(is_published=True)
    
    # Pobieramy wartość parametru 'q' z żądania GET (jeśli nie istnieje, zwróci None)
    query = request.GET.get('q')
    
    # Jeśli użytkownik coś wpisał, filtrujemy wyniki
    if query:
        # title__icontains sprawdza, czy pole title zawiera szukaną frazę (niezależnie od wielkości liter)
        articles = articles.filter(title__icontains=query)
    
    three_days_ago = timezone.now() - timedelta(days=3)
    
    context = {
        'articles': articles,
        'three_days_ago': three_days_ago,
        'search_query': query # Przekazujemy zapytanie do szablonu, aby zapamiętać wpisany tekst w polu
    }
    return render(request, 'articles/article_list.html', context)



# do - articles/templates/articles/article_list.html

{% extends "base.html" %}

{% block content %}
    <h1>Lista Artykułów</h1>
    
    <!-- Formularz wyszukiwania -->
    <form method="GET" action="" class="mt-4 mb-4">
        <div class="input-group">
            <input type="text" name="q" class="form-control" placeholder="Szukaj po tytule..." value="{{ search_query|default_if_none:'' }}">
            <button class="btn btn-primary" type="submit">Szukaj</button>
            
            {% if search_query %}
                <a href="/articles/" class="btn btn-outline-secondary">Wyczyść</a>
            {% endif %}
        </div>
    </form>
    
    <!-- Lista artykułów -->
    <ul class="list-group">
        {% for article in articles %}
            <li class="list-group-item">
                <strong>{{ article.title }}</strong>
                
                {% if article.created_at >= three_days_ago %}
                    <span class="badge bg-danger ms-2">NOWOŚĆ!</span>
                {% endif %}
                
                <p class="mb-0 mt-2">{{ article.content|truncatewords:10 }}</p>
            </li>
        {% empty %}
            <li class="list-group-item">Brak artykułów do wyświetlenia.</li>
        {% endfor %}
    </ul>
    
    <a href="/categories/" class="btn btn-secondary mt-3">Przejdź do kategorii</a>
{% endblock %}



http://127.0.0.1:8000/articles/