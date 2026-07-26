# projekt_auth/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Wbudowane widoki logowania i wylogowania (korzystają z szablonów, które zaraz dodamy)
    path('login/', auth_views.LoginView.as_view(template_name='konta/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='konta/logout.html'), name='logout'),
    
    # Podłączam adresy z naszej aplikacji konta
    path('', include('konta.urls')),
]