from django.urls import path
from . import views
from myapp.views import info_view, product_list_view, note_list_view, note_detail_view, add_product_view


urlpatterns = [
    path('info/', views.info_view, name='info'),
    path('rules/', views.rules_view, name='rules'),
    # Zadanie 2. Nowa trasa dynamiczna:
    path('user/<str:username>/', views.user_profile_view, name='user-profile'), 
    path('products/', views.product_list_view, name='product-list'),
    path('notes/', note_list_view, name='note_list'),
    path('note/<int:note_id>/', note_detail_view, name='note_detail'),
    path('add-product/', add_product_view, name='add_product'),
]

