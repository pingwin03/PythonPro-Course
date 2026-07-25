from django.urls import path
from . import views

urlpatterns = [
    # Ścieżka do strony głównej (Zadanie 3)
    path('', views.home, name='home'),
    # Definiuje ścieżkę z parametrem category_id
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
]