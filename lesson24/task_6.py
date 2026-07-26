# Zadanie 6 – Rozszerzenie formularza rejestracji (challenge)
# Stwórz własny formularz w pliku forms.py, dziedzicząc po UserCreationForm. Dodaj do
# niego pole email. Następnie w widoku register użyj swojego nowego formularza zamiast
# domyślnego. Upewnij się, że email jest wymagany i zapisywany w bazie danych





# konta/forms.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegisterForm(UserCreationForm):
    # Dodajemy pole email, ustawiając je jako wymagane
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        # Określamy pola, które pojawią się w formularzu rejestracyjnym
        fields = ['username', 'email']
        
        
        
        
        # konta/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    # Zadanie 6: Obsługa własnego formularza rejestracji z polem email
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Zapisuje użytkownika oraz adres e-mail w bazie danych
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto zostało utworzone dla {username}! Możesz się teraz zalogować.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    return render(request, 'konta/register.html', {'form': form})



# konta/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),  # <--- Nowa ścieżka
]



# konta/templates/konta/register.html

<!-- konta/templates/konta/register.html -->
{% extends "konta/base.html" %}
{% block content %}
<div class="content-section">
    <form method="POST">
        {% csrf_token %}
        <fieldset class="form-group">
            <legend class="border-bottom mb-4">Dołącz do nas</legend>
            {{ form.as_p }}
        </fieldset>
        <div class="form-group">
            <button class="btn btn-outline-info" type="submit">Zarejestruj się</button>
        </div>
    </form>
    <div class="border-top pt-3">
        <small class="text-muted">
            Masz już konto? <a class="ml-2" href="{% url 'login' %}">Zaloguj się</a>
        </small>
    </div>
</div>
{% endblock content %}


# konta/templates/konta/base.html


{% else %}
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'login' %}">Zaloguj</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'register' %}">Zarejestruj</a>
                    </li>
                {% endif %}
                
                


http://127.0.0.1:8000/register/