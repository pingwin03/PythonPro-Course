# konta/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    # Nowa ścieżka dla panelu użytkowników (tylko dla staff)
    path('admin-users/', views.admin_user_list, name='admin_user_list'),
    
    # Zadanie 8: Widoki zmiany hasła
    path('password-change/', 
         auth_views.PasswordChangeView.as_view(template_name='konta/password_change_form.html'), 
         name='password_change'),
         
    path('password-change/done/', 
         auth_views.PasswordChangeDoneView.as_view(template_name='konta/password_change_done.html'), 
         name='password_change_done'),
]