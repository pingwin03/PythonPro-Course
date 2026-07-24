# Zadanie 8 – Logika warunkowa w szablonie
# Dodaj do modelu Article pole is_published typu BooleanField z default=True. W widoku listy
# artykułów pobieraj tylko te, które są opublikowane (is_published=True). W szablonie
# article_list.html dodaj obok tytułu każdego artykułu napis "NOWOŚĆ!" (np. w ), ale tylko jeśli
# artykuł został opublikowany w ciągu ostatnich 3 dni.
# Wskazówka: Możesz potrzebować niestandardowego tagu szablonu lub przekazać
# dodatkową informację z widoku. Prostsze rozwiązanie: użyj wbudowanego filtra timesince
# lub timeuntil.

# do - articles/models.py

from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    
    # Nowe pola do Zadania 8:
    is_published = models.BooleanField(default=True)
    # auto_now_add=True automatycznie zapisze datę przy tworzeniu artykułu
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title

 
#  w terminalu.   
python manage.py makemigrations
python manage.py migrate

# do articles/views.py


from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Category, Article

# ... (poprzednie widoki kategorii zostają bez zmian) ...

def article_list_view(request):
    # Pobieramy TYLKO opublikowane artykuły
    published_articles = Article.objects.filter(is_published=True)
    
    # Obliczamy datę sprzed 3 dni
    three_days_ago = timezone.now() - timedelta(days=3)
    
    context = {
        'articles': published_articles,
        'three_days_ago': three_days_ago
    }
    return render(request, 'articles/article_list.html', context)

# do - le21/urls.py

from django.contrib import admin
from django.urls import path
# nowy widok:
from articles.views import category_list_view, category_detail_view, article_list_view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', category_list_view, name='category-list'),
    path('categories/<int:pk>/', category_detail_view, name='category-detail'),
    # Nowa ścieżka dla artykułów:
    path('articles/', article_list_view, name='article-list'), 
]

# do - articles/templates/articles/ tworzę nowy plik o nazwie article_list.html

{% extends "base.html" %}

{% block content %}
    <h1>Lista Artykułów</h1>
    
    <ul class="list-group mt-4">
        {% for article in articles %}
            <li class="list-group-item">
                <strong>{{ article.title }}</strong>
                
                <!-- Logika warunkowa: jeśli artykuł utworzono później/równo z datą 3 dni temu -->
                {% if article.created_at >= three_days_ago %}
                    <span class="badge bg-danger ms-2">NOWOŚĆ!</span>
                {% endif %}
                
                <p class="mb-0 mt-2">{{ article.content|truncatewords:10 }}</p>
            </li>
        {% empty %}
            <li class="list-group-item">Brak opublikowanych artykułów.</li>
        {% endfor %}
    </ul>
    
    <a href="/categories/" class="btn btn-secondary mt-3">Przejdź do kategorii</a>
{% endblock %}



http://127.0.0.1:8000/articles/