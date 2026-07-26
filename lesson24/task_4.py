# Zadanie 4 – Komunikaty messages (proste)
# Upewnij się, że w Twoim szablonie bazowym (base.html) masz pętlę, która wyświetla
# komunikaty z frameworka messages Django. Dzięki temu komunikat o pomyślnej rejestracji,
# który dodaliśmy w widoku, faktycznie się pojawi

# {% if messages %}
# {% for message in messages %}
# <div class="alert alert-{{ message.tags }}">
# {{ message }}
# </div>
# {% endfor %}
# {% endif %}




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
        <!-- Zadanie 4: Dodaję pętlę wyświetlającą komunikaty systemowe -->
        {% if messages %}
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }}">
                    {{ message }}
                </div>
            {% endfor %}
        {% endif %}

        {% block content %}
        {% endblock %}
    </div>
</body>
</html>