"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import ProtectedUserView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Dodane przeze mnie ścieżki:
    path('auth/', include('djoser.urls')), 
    path('auth/', include('djoser.urls.jwt')), # Ścieżki do logowania/odświeżania JWT
    # Dodaję nową ścieżkę do mojego chronionego endpointu
    path('api/protected/', ProtectedUserView.as_view(), name='protected_view'),
]

