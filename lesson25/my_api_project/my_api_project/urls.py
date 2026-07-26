"""
URL configuration for my_api_project project.

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
# Importuję widoki z mojej aplikacji, aby móc je zarejestrować
from products_app import views 

# Tworzę instancję routera, który zajmie się adresami
router = DefaultRouter()


# Rejestruję mój ViewSet pod ścieżką 'products'
router.register(r'products', views.ProductViewSet, basename='product')

# Dodaję nową linijkę, aby zarejestrować endpoint dla notatek
router.register(r'notes', views.NoteViewSet)

# Rejestruję endpointy dla autorów i książek
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Podłączam wszystkie wygenerowane adresy z routera pod prefiks 'api/'
    path('api/', include(router.urls)),
    # Dodaję ścieżkę do kalkulatora
    path('api/calculate/', views.calculate_view),
    # Dodaję moje nowe ścieżki dla zadań z ciasteczkami
    path('api/set-name/', views.set_name_view),
    path('api/hello/', views.hello_view),
]
