# Zadanie 3 – Strona profilu (proste)
# Stwórz prosty widok profile, który będzie renderował szablon profile.html. W szablonie
# wyświetl powitanie, używając nazwy zalogowanego użytkownika, np.
# Witaj, {{ user.username }}!
# . Zabezpiecz ten widok dekoratorem @login_required




# konta/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    # Zadanie 3: Ten widok jest dostępny tylko dla zalogowanych użytkowników
    return render(request, 'konta/profile.html')




<!-- konta/templates/konta/profile.html -->
{% extends "konta/base.html" %}

{% block content %}
<div class="content-section">
    <!-- Zadanie 3: Wyświetlam powitanie z nazwą zalogowanego użytkownika[cite: 1] -->
    <h2>Witaj, {{ user.username }}!</h2>
    <p>To jest Twój panel profilowy.</p>
</div>
{% endblock content %}