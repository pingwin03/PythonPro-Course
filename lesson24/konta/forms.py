# konta/forms.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegisterForm(UserCreationForm):
    # Dodaje pole email, ustawiając je jako wymagane
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        # Określam pola, które pojawią się w formularzu rejestracyjnym
        fields = ['username', 'email']