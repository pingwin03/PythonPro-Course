# Zadanie 4 – Plik statyczny CSS
# Stwórz plik style.css w odpowiednim katalogu static. Dodaj do niego regułę, która
# zmienia kolor tła strony (body { background-color: #f0f8ff ; }). Podłącz ten plik CSS do
# szablonu z listą kategorii.



# do - po stworzeniu articles/static/articles/style.css.
body { 
    background-color: #f0f8ff; 
}

# do - articles/templates/articles/category_list.html


{% extends "base.html" %}
{% load static %}

{% block content %}
    <!-- Link do pliku CSS -->
    <link rel="stylesheet" href="{% static 'articles/style.css' %}">

    <h1>Lista Kategorii</h1>
    
    {% if categories %}
        <ul>
            {% for category in categories %}
                <li>{{ category.name }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>Brak kategorii w bazie.</p>
    {% endif %}
{% endblock %}


http://127.0.0.1:8000/categories/