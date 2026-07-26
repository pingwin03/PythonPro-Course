# Zadanie 8 – Chroniony endpoint
# Stwórz prosty widok w DRF (APIView), który będzie dostępny tylko dla zalogowanych
# użytkowników. W tym celu ustaw permission_classes = [IsAuthenticated]. Widok powinien
# zwracać nazwę zalogowanego użytkownika (request.user.username). Przetestuj go w
# Postmanie – najpierw bez tokenu (powinieneś otrzymać błąd 401), a potem z poprawnym
# Authorization: Bearer w nagłówku



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ProtectedUserView(APIView):
    # Wymagam, aby użytkownik był zalogowany
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Pobieram i zwracam nazwę użytkownika z obiektu request
        return Response({
            "username": request.user.username
        })
        
        
        
from django.contrib import admin
from django.urls import path, include
from core.views import ProtectedUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    
    # Dodaję nową ścieżkę do mojego chronionego endpointu
    path('api/protected/', ProtectedUserView.as_view(), name='protected_view'),
]


test  zrzuty ekranu dwa
http://127.0.0.1:8000/api/protected/