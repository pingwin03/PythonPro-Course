from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Note, Category # Importujemy nasz model
from .forms import ProductForm
from django.core.paginator import Paginator

# Create your views here.
from django.http import HttpResponse

def info_view(request):
    return render(request, 'myapp/info.html')

def rules_view(request):
    return HttpResponse("Regulamin")
# Zadanie 2
def user_profile_view(request, username):
    return HttpResponse(f"Witaj na profilu, {username}!")


def product_list_view(request):
    # Wyciągamy wszystkie produkty z bazy
    products = Product.objects.all()
    # Przekazujemy je do szablonu za pomocą słownika
    return render(request, 'myapp/product_list.html', {'products': products})


# Widok 1: Lista wszystkich notatek
def note_list_view(request):
    # 1. Pobieramy wszystkie notatki i sortujemy je od najnowszych
    note_list = Note.objects.all().order_by('-id')
    
    # 2. Tworzymy obiekt Paginatora i mówimy mu: "3 notatki na jedną stronę"
    paginator = Paginator(note_list, 3)
    
    # 3. Sprawdzamy, na której stronie aktualnie jest użytkownik (z adresu np. ?page=2)
    page_number = request.GET.get('page')
    
    # 4. Pobieramy notatki tylko dla wybranej strony
    page_obj = paginator.get_page(page_number)
    
    # 5. Zamiast 'notes', do szablonu przekazujemy nasz nowy obiekt 'page_obj'
    return render(request, 'myapp/note_list.html', {'page_obj': page_obj})

# Widok 2: Szczegóły pojedynczej notatki
def note_detail_view(request, note_id):
    # get_object_or_404 to bezpieczny sposób pobierania - wyrzuci błąd 404, jeśli notatka nie istnieje
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'myapp/note_detail.html', {'note': note})



def add_product_view(request):
    if request.method == 'POST':
        # Jeśli użytkownik wysłał dane, wypełniamy formularz tymi danymi
        form = ProductForm(request.POST)
        if form.is_valid():
            # Jeśli dane są poprawne, zapisujemy nowy produkt w bazie
            form.save()
            # Przekierowujemy na stronę z listą produktów 
            return redirect('/products/') 
    else:
        # Jeśli użytkownik dopiero wszedł na stronę (GET), pokazujemy pusty formularz
        form = ProductForm()
    
    return render(request, 'myapp/add_product.html', {'form': form})


# Nowy widok
def category_products_view(request, category_id):
    # Pobieramy konkretną kategorię po jej ID. Jeśli ktoś wpisze zły ID w URL, Django bezpiecznie zwróci błąd 404
    category = get_object_or_404(Category, id=category_id)
    
    # Filtrujemy produkty przypisane do tej właśnie kategorii
    products = Product.objects.filter(category=category)
    
    # Przekazujemy przefiltrowaną listę oraz sam obiekt kategorii do szablonu
    context = {
        'products': products,
        'category': category
    }
    return render(request, 'myapp/category_products.html', context)

