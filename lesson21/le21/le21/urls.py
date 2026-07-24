"""
URL configuration for le21 project.

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
from articles.views import category_list_view, category_detail_view, article_list_view # Importujemy nasz nowy widok

urlpatterns = [
    path('admin/', admin.site.urls),
# Podłączamy widok pod URL /categories/
    path('categories/', category_list_view, name='category-list'),
    # Nowa ścieżka dla szczegółów kategorii (oczekuje liczby całkowitej <int:pk>)
    path('categories/<int:pk>/', category_detail_view, name='category-detail'),
    path('articles/', article_list_view, name='article-list'),
]

