# Zadanie 4 – Konfiguracja URLi
# Skonfiguruj główny plik urls.py swojego projektu, aby zawierał ścieżki URL dostarczane
# przez bibliotekę Djoser dla uwierzytelniania i obsługi JWT.



# core/urls.py
from django.contrib import admin #[cite: 1]
from django.urls import path, include #[cite: 1]

urlpatterns = [
    path('admin/', admin.site.urls), #[cite: 1]
    
    # Dodane przeze mnie ścieżki:
    path('auth/', include('djoser.urls')), #[cite: 1]
    path('auth/', include('djoser.urls.jwt')), # Ścieżki do logowania/odświeżania JWT[cite: 1]
]