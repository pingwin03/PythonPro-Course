from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.db.models import Q


def category_posts(request, category_id):
    # Pobieram kategorię na podstawie ID z adresu URL (lub zwracamy błąd 404)
    category = get_object_or_404(Category, id=category_id)
    
    # Używam metody filter(), aby pobrać tylko posty z tej kategorii
    posts = Post.objects.filter(category=category)
    
    # Przekazuje dane do szablonu HTML
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/category_posts.html', context)



# Zaktualizowany widok dla Zadania 6
def home(request):
    # Pobieram frazę z parametru 'q' (request.GET to słownik z parametrami URL)
    query = request.GET.get('q')
    
    if query:
        # Jeśli użytkownik czegoś szuka, filtrujemy tytuł LUB treść
        # Używam __icontains, aby ignorować wielkość liter
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).order_by('-publication_date')
    else:
        # Jeśli nie ma zapytania, pokazuje 5 najnowszych (jak w Zadaniu 3)
        posts = Post.objects.order_by('-publication_date')[:5]
    
    context = {
        'posts': posts,
        'query': query, # Przekazuje frazę do szablonu, by ją tam wyświetlić
    }
    return render(request, 'blog/home.html', context)