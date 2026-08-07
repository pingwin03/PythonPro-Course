"""
URL configuration for cache_project project.

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
from rest_framework.routers import DefaultRouter
from store.views import product_list, selective_cache_view, ProductViewSet

# Konfiguruję router dla mojego ViewSetu
router = DefaultRouter()
router.register(r'api/products', ProductViewSet, basename='api-product')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ścieżka dla Django Debug Toolbar (niezbędna do podglądu zapytań i zakładki Cache)
    path('__debug__/', include('debug_toolbar.urls')),
    
    # Endpoint z Zadania 3 (cachowanie całej odpowiedzi za pomocą dekoratora @cache_page)
    path('products/', product_list, name='product-list'),
    
    # Endpoint z Zadania 7 (selektywne cachowanie z użyciem niskopoziomowego API)
    path('selective/', selective_cache_view, name='selective-cache'),
    # Podpinam wszystkie ścieżki wygenerowane przez router (w tym list, retrieve, create itp.)
    path('', include(router.urls)),
]