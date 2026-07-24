# Zadanie 7 – Relacja i wyświetlanie
# Zmodyfikuj model Article, dodając do niego pole category typu ForeignKey do modelu
# Category (on_delete=models.CASCADE). Przypisz w shellu każdemu artykułowi jakąś
# kategorię. Następnie zmodyfikuj szablon category_detail.html tak, aby pod nazwą kategorii
# wyświetlał listę wszystkich artykułów należących do tej kategorii.
# Wskazówka: Po stworzeniu relacji, z obiektu kategorii możesz odwołać się do powiązanych
# artykułów przez category.article_set.all()


# do - articles/models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    # Dodajemy klucz obcy do modelu Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
    

# Migracja w terminalu
python manage.py makemigrations
python manage.py migrate

# w python manage.py shell
from articles.models import Category, Article

# Pobieramy przykładową kategorię, np. "Technologia"
tech_category = Category.objects.get(name="Technologia")

# Tworzymy nowe artykuły przypisane do tej kategorii
Article.objects.create(title="Nowości w Pythonie", content="Treść artykułu...", category=tech_category)
Article.objects.create(title="Django dla początkujących", content="Treść...", category=tech_category)

exit()

# do articles/templates/articles/category_detail.html

{% extends "base.html" %}

{% block content %}
    <h1>{{ category.name }}</h1>
    
    <h3 class="mt-4">Artykuły w tej kategorii:</h3>
    <ul>
        <!-- Używamy relacji odwrotnej (article_set.all), aby pobrać artykuły -->
        {% for article in category.article_set.all %}
            <li>
                <strong>{{ article.title }}</strong> - {{ article.content|truncatewords:5 }}
            </li>
        {% empty %}
            <li>Brak artykułów w tej kategorii.</li>
        {% endfor %}
    </ul>
    
    <a href="/categories/" class="btn btn-secondary mt-3">Powrót do listy</a>
{% endblock %}