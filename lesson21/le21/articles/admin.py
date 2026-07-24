from django.contrib import admin
from .models import Category, Article

# Rejestracja modeli (jeśli jeszcze tego nie zrobiłeś)
admin.site.register(Category)
admin.site.register(Article)

# # Zmiana nagłówków w panelu admina:
# admin.site.site_header = "Panel Administratora Mojej Strony"
# admin.site.site_title = "Panel Administratora Mojej Strony"
# admin.site.index_title = "Witaj w panelu zarządzania treścią"