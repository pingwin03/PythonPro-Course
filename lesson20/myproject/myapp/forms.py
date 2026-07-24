from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # Zakładam model Product ma pola 'name' i 'price' na podstawie wcześniejszych zadań
        fields = ['name', 'price']