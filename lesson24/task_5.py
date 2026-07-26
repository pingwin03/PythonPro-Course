
# Zadanie 5 – Strona główna tylko dla zalogowanych (proste)
# Zabezpiecz widok strony głównej Twojej aplikacji za pomocą dekoratora @login_required,
# tak aby była ona dostępna tylko dla zalogowanych użytkowników.



# konta/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'konta/profile.html')

@login_required
def home(request):
    # Zadanie 5: Zabezpieczam widok strony głównej dekoratorem, dostępny tylko dla zalogowanych
    return render(request, 'konta/home.html')





<!-- konta/templates/konta/home.html -->
{% extends "konta/base.html" %}

{% block content %}
<div class="content-section">
    <h2>Strona Główna</h2>
    <p>Witaj w zabezpieczonej strefie aplikacji, {{ user.username }}!</p>
</div>
{% endblock content %}