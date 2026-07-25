# Zadanie 2 – Widok Kategorii
# Napisz widok, który po wejściu na URL /category/<category_id>/ wyświetli listę wszystkich
# postów należących do danej kategorii. Użyj metody filter() na QuerySet. (proste)


# Napisanie widoku (blog/views.py)

from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def category_posts(request, category_id):
    # Pobieram kategorię na podstawie ID z adresu URL (lub zwracamy błąd 404)
    category = get_object_or_404(Category, id=category_id)
    
    # Używam metody filter(), aby pobrać tylko posty z tej kategorii
    posts = Post.objects.filter(category=category)
    
    # Przekazujem dane do szablonu HTML
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/category_posts.html', context)


# Podłączenie adresu URL (urls.py)


from django.urls import path
from . import views

urlpatterns = [
    # Definiuje ścieżkę z parametrem category_id
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
]

# do - blog_project/urls.py informuje projekt o adresach

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # Dołączamy adresy naszej aplikacji
]

# Wyświetlanie wyników W folderze blog tworzę nowy folder o nazwie templates
# wewnątrz folderu templates tworzę kolejny folder o nazwie blog
# wewnątrz folderu blog (czyli ścieżka to blog/templates/blog/) tworzę plik category_posts.html

<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Kategoria: {{ category.name }}</title>
</head>
<body>
    <h1>Posty w kategorii: {{ category.name }}</h1>
    
    {% if posts %}
        <ul>
            {% for post in posts %}
                <li>
                    <strong>{{ post.title }}</strong> 
                    (Data: {{ post.publication_date|date:"d.m.Y" }})
                </li>
            {% endfor %}
        </ul>
    {% else %}
        <p>Brak postów w tej kategorii.</p>
    {% endif %}
</body>
</html>