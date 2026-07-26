# Zadanie 7 – Tworzenie własnego Middleware
# Stwórz prosty, własny middleware, który dla każdego przychodzącego zapytania będzie
# dodawał do konsoli (użyj print()) informację o metodzie HTTP, z jakiej skorzystano (np.
# "Otrzymano zapytanie metodą GET"). Pamiętaj, aby dodać swoje middleware do listy
# MIDDLEWARE w settings.py.




Najpierw muszę stworzyć miejsce na mój kod. W folderze core 
(tam, gdzie znajduje się mój plik settings.py), tworzę nowy plik o nazwie middleware.py.


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
    
    
    
# core/settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # Moje własne middleware:
    'core.middleware.HttpMethodLoggingMiddleware',
]