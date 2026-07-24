# Zadanie 2 – Stwórz dynamiczną trasę
# Dodaj dynamiczną trasę /user/<str:username>/, która przyjmie nazwę użytkownika jako ciąg
# znaków. Stwórz widok, który wyświetli komunikat powitalny, np. "Witaj na profilu,
# username!"


# kod do pliku: myapp/views.py
def user_profile_view(request, username):
    return HttpResponse(f"Witaj na profilu, {username}!")



# kod do pliku: myapp/urls.py zaktualizowanie listy
from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info_view, name='info'),
    path('rules/', views.rules_view, name='rules'),
    # Nowa trasa dynamiczna:
    path('user/<str:username>/', views.user_profile_view, name='user-profile'), 
]