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