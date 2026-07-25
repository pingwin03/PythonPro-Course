# Zadanie 3 – Ostatnie Posty na Stronie Głównej
# Zmodyfikuj widok strony głównej tak, aby wyświetlał tylko 5 najnowszych postów. Użyj
# order_by() i "krojenia" (slicing) QuerySetu. (proste)


# Do - blog/views.py: dodajemy nowy widok
    
    
from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def home(request):
    # Pobieram 5 najnowszych postów
    latest_posts = Post.objects.order_by('-publication_date')[:5]
    
    context = {
        'posts': latest_posts
    }
    return render(request, 'blog/home.html', context)



# Podłączenie widoku do adresu URL (blog/urls.py)
from django.urls import path
from . import views

urlpatterns = [
    # Ścieżka do strony głównej (Zadanie 3)
    path('', views.home, name='home'),
    
    # Ścieżka do widoku kategorii (Zadanie 2)
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
]


# W folderze blog/templates/blog/ tworzę nowy plik o nazwie home.html

<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Strona Główna Bloga</title>
</head>
<body>
    <h1>Ostatnie posty na blogu</h1>
    
    {% if posts %}
        <ul>
            {% for post in posts %}
                <li>
                    <strong>{{ post.title }}</strong> 
                    <br>
                    <small>Data publikacji: {{ post.publication_date|date:"d.m.Y H:i" }} | Autor: {{ post.author.name }}</small>
                </li>
            {% endfor %}
        </ul>
    {% else %}
        <p>Brak postów na blogu.</p>
    {% endif %}
</body>
</html>


http://127.0.0.1:8000/