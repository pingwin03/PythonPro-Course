# Zadanie 9 – Zmiana w panelu admina
# Domyślnie tytuł w panelu admina to "Django administration". Znajdź w internecie, jak
# nadpisać szablon admin/base.html, aby zmienić ten tytuł na "Panel Administratora Mojej
# Strony".



# 1. W głównym katalogu projektu (tam, gdzie masz folder le21 i plik manage.py) 
# upewnij się, że masz folder na szablony globalne
# 2. Wewnątrz tego folderu stwórz strukturę podfolderów: templates/admin/
# 3. W folderie admin/ utwórz nowy plik o nazwie base_site.html.

# wpisujemy


{% extends "admin/base.html" %}

{% block branding %}
<h1 id="site-name">
    <a href="{% url 'admin:index' %}">Panel Administratora Mojej Strony</a>
</h1>
{% endblock %}

