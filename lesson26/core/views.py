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