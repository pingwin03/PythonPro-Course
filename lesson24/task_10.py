# Zadanie 10 – Widok tylko dla admina (challenge)
# Stwórz widok, który będzie wyświetlał listę wszystkich zarejestrowanych użytkowników
# (User.objects.all()). Ogranicz dostęp do tego widoku tak, aby mogli go zobaczyć tylko
# użytkownicy, którzy mają status "staff" (is_staff=True). (Wskazówka: użyj dekoratora
# @staff_member_required z django.contrib.admin.views.decorators).



# konta/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required  # <--- 1. Importuję dekorator dla personelu
from django.contrib.auth.models import User  # <--- 2. Importuję domyślny model User
from .forms import UserRegisterForm

@login_required
def profile(request):
    return render(request, 'konta/profile.html')

@login_required
def home(request):
    return render(request, 'konta/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto zostało utworzone dla {username}! Zostałeś automatycznie zalogowany.')
            return redirect('home')
    else:
        form = UserRegisterForm()
    
    return render(request, 'konta/register.html', {'form': form})

# Zadanie 10: Widok dostępny tylko dla użytkowników ze statusem staff
@staff_member_required
def admin_user_list(request):
    users = User.objects.all()  # Pobieram wszystkich użytkowników z bazy
    return render(request, 'konta/admin_user_list.html', {'users': users})


# Dodać ścieżkę (URL) w pliku konta/urls.py

# konta/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    # Nowa ścieżka dla panelu użytkowników (tylko dla staff)
    path('admin-users/', views.admin_user_list, name='admin_user_list'),
]



# <!-- konta/templates/konta/admin_user_list.html -->
{% extends "konta/base.html" %}
{% block content %}
<div class="content-section">
    <h2>Panel Administratora – Lista Użytkowników</h2>
    <p class="text-secondary">Widok dostępny wyłącznie dla personelu (is_staff = True).</p>
    
    <table class="table table-striped mt-3">
        <thead>
            <tr>
                <th>ID</th>
                <th>Nazwa użytkownika</th>
                <th>E-mail</th>
                <th>Status Staff</th>
                <th>Superużytkownik</th>
            </tr>
        </thead>
        <tbody>
            {% for u in users %}
            <tr>
                <td>{{ u.id }}</td>
                <td>{{ u.username }}</td>
                <td>{{ u.email }}</td>
                <td>{% if u.is_staff %}Tak{% else %}Nie{% endif %}</td>
                <td>{% if u.is_superuser %}Tak{% else %}Nie{% endif %}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>
{% endblock content %}



http://127.0.0.1:8000/admin-users/