# Zadanie 9 – Automatyczne logowanie po rejestracji (challenge)
# Zmodyfikuj widok register tak, aby po pomyślnym utworzeniu konta użytkownik był od razu
# logowany. (Wskazówka: zaimportuj i użyj funkcji login z django.contrib.auth).



# konta/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login  # <--- Importuję funkcję login
from django.contrib.auth.decorators import login_required
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
            user = form.save()  # Zapisuję użytkownika i przypisuję do zmiennej
            
            # Automatycznie loguję użytkownika tuż po rejestracji
            login(request, user)
            
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto zostało utworzone dla {username}! Zostałeś automatycznie zalogowany.')
            return redirect('home')  # Przekierowuję na stronę główną
    else:
        form = UserRegisterForm()
    
    return render(request, 'konta/register.html', {'form': form})