"""
URL configuration for myproject project.

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
from myapp.views import category_products_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')), # Przekierowujemy ruch do aplikacji 'myapp'
    # <int:category_id> to dynamiczny parametr. Django wyciągnie z URL-a liczbę (int) 
    # i przekaże ją do funkcji widoku jako argument "category_id"
    path('category/<int:category_id>/', category_products_view, name='category_products'),
]

