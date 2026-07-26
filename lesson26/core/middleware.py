# core/middleware.py

class HttpMethodLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response #
        # Jednorazowa konfiguracja i inicjalizacja

    def __call__(self, request):
        # Ten kod wykona się dla każdego zapytania, zanim dotrze do widoku
        print(f"Otrzymano zapytanie metodą {request.method}")
        
        response = self.get_response(request) 
        
        return response 