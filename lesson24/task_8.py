# Zadanie 8 – Zmiana hasła (challenge)
# Wykorzystaj wbudowane widoki Django: PasswordChangeView i
# PasswordChangeDoneView do stworzenia funkcjonalności zmiany hasła przez
# zalogowanego użytkownika. Będziesz musiał dodać odpowiednie ścieżki w urls.py i
# stworzyć dwa proste szablony (password_change_form.html i
# password_change_done.html)


# konta/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    
    # Zadanie 8: Widoki zmiany hasła
    path('password-change/', 
         auth_views.PasswordChangeView.as_view(template_name='konta/password_change_form.html'), 
         name='password_change'),
         
    path('password-change/done/', 
         auth_views.PasswordChangeDoneView.as_view(template_name='konta/password_change_done.html'), 
         name='password_change_done'),
]




# Stworzenie szablonu formularza zmiany hasła
<!-- konta/templates/konta/password_change_form.html -->
{% extends "konta/base.html" %}
{% block content %}
<div class="content-section">
    <form method="POST">
        {% csrf_token %}
        <fieldset class="form-group">
            <legend class="border-bottom mb-4">Zmiana hasła</legend>
            {{ form.as_p }}
        </fieldset>
        <div class="form-group">
            <button class="btn btn-outline-info" type="submit">Zmień hasło</button>
        </div>
    </form>
</div>
{% endblock content %}



# Stworzenie szablonu potwierdzenia (password_change_done.html)

<!-- konta/templates/konta/password_change_done.html -->
{% extends "konta/base.html" %}
{% block content %}
<div class="alert alert-success">
    Twoje hasło zostało pomyślnie zmienione!
</div>
<p><a href="{% url 'profile' %}" class="btn btn-outline-info">Wróć do profilu</a></p>
{% endblock content %}


# Dodanie linku w szablonie profilu (profile.html)

<p><a href="{% url 'password_change' %}">Zmień hasło</a></p>