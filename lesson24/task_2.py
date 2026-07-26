# Zadanie 2 – Linki w nawigacji (proste)
# Zmodyfikuj swój szablon bazowy (base.html), aby dynamicznie wyświetlać linki. Jeśli
# użytkownik jest zalogowany (user.is_authenticated), pokaż linki do "Profilu" i "Wyloguj". Jeśli
# nie jest zalogowany, pokaż linki "Zaloguj" i "Zarejestruj"


# Najpierw tworzę strukturę katalogów na szablony w naszej aplikacji konta:
# konta/templates/konta/base.html


<!-- konta/templates/konta/base.html -->
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Moja Aplikacja</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="{% url 'home' %}">Strona Główna</a>
        <div class="collapse navbar-collapse">
            <ul class="navbar-nav ml-auto">
                <!-- Zadanie 2: Sprawdzam, czy użytkownik jest zalogowany -->
                {% if user.is_authenticated %}
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'profile' %}">Profil</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'logout' %}">Wyloguj</a>
                    </li>
                {% else %}
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'login' %}">Zaloguj</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'register' %}">Zarejestruj</a>
                    </li>
                {% endif %}
            </ul>
        </div>
    </nav>

    <div class="container mt-4">
        {% block content %}
        {% endblock %}
    </div>
</body>
</html>