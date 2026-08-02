"""
URL configuration for my_project project.

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
from django.urls import path
from django.conf import settings # <--- Importuję moje ustawienia
from django.conf.urls.static import static # <--- Importuję funkcję static
from my_app import views # <--- Importuję moje widoki
from my_app.views import create_user_with_transaction



urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ustawiam ścieżkę 'hello/', po wejściu na którą wywołam mój widok trigger_hello_world
    path('hello/', views.trigger_hello_world, name='hello_world'),
    
    # Dodaję nową ścieżkę dla formularza mnożenia
    path('multiply/', views.multiply_view, name='multiply'),
    path('log/', views.log_view, name='log_timestamp'),
    path('count-users/', views.count_users_view, name='count_users'),
    path('update-login/', views.update_login_view, name='update_login'),
    path('process-video/', views.process_video_view, name='process_video'),
    path('send-email/', views.trigger_email_view, name='send_email'),
    
    # Ścieżki paska postępu z Zadania 11
    path('start-progress/', views.start_progress_view, name='start_progress'),
    path('task-status/<str:task_id>/', views.task_status_view, name='task_status'),
    
    # Dodaję nowe ścieżki do generowania raportu CSV z Zadania 14
    path('start-csv/', views.start_csv_report_view, name='start_csv'),
    path('check-csv/<str:task_id>/', views.check_csv_report_view, name='check_csv'),
    # Ścieżka do testowania ponawiania zadań z Zadania 15
    path('test-retry/', views.start_retry_task_view, name='start_retry'),
    path('upload-image/', views.upload_image_view, name='upload_image'),
    path('test-chain/', views.start_chain_view, name='start_chain'),
    path('test-queues/', views.test_queues_view, name='test_queues'),
    path('test-transaction/', create_user_with_transaction, name='test_transaction'),
]

# Pozwalam Django na serwowanie plików z folderu media w trybie deweloperskim
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)