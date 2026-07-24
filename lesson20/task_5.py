# Zadanie 5 – Stwórz szablon bazowy
# Stwórz plik base.html z podstawową strukturą HTML, zawierający bloki {% block title %}
# i {% block content %}. Następnie stwórz drugi szablon, który będzie dziedziczył po
# base.html i uzupełni te bloki własną treścią.

# :\PythonPro-Course\homework\lesson20\myproject\myapp\templates\myapp\
    
    
#     base.html
    
    <!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Domyślny Tytuł{% endblock %}</title>
</head>
<body>
    <header>
        <h2>Menu główne naszej strony</h2>
        <hr>
    </header>

    <main>
        <!-- Tutaj będzie trafiać unikalna treść z innych szablonów -->
        {% block content %}
        {% endblock %}
    </main>

    <footer>
        <hr>
        <p>Stopka strony (widoczna wszędzie)</p>
    </footer>
</body>
</html>


# myapp/templates/myapp/

# info.html
{% extends "myapp/base.html" %}

{% block title %}Strona Informacyjna{% endblock %}

{% block content %}
    <h1>Witaj na stronie informacyjnej!</h1>
    <p>Ta treść została wstawiona do bloku 'content' z szablonu bazowego.</p>
{% endblock %}



# http://127.0.0.1:8000/info/