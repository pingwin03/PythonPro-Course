# Zadanie 1 – Stwórz statyczne trasy i widoki
# Stwórz w swojej aplikacji Django dwie statyczne trasy: /info/ oraz /rules/. Każda z nich
# powinna prowadzić do osobnego widoku opartego na funkcji, który zwraca prosty tekst w
# HttpResponse (np. "Informacje o stronie" i "Regulamin").

# do pliku:myapp/views.py
from django.http import HttpResponse

def info_view(request):
    return HttpResponse("Informacje o stronie")

def rules_view(request):
    return HttpResponse("Regulamin")

# do pliku:  myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info_view, name='info'),
    path('rules/', views.rules_view, name='rules'),
]