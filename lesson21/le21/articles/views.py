from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Category, Article

def category_list_view(request):
    # Pobieramy wszystkie kategorie z bazy
    all_categories = Category.objects.all()
    
    # Przekazujemy dane do szablonu za pomocą słownika kontekstu
    context = {
        'categories': all_categories
    }
    return render(request, 'articles/category_list.html', context)


def category_detail_view(request, pk):
    # Pobieramy z bazy konkretną kategorię na podstawie ID (pk)
    category = Category.objects.get(id=pk)
    
    # Przekazujemy pobraną kategorię do szablonu
    context = {
        'category': category
    }
    
    return render(request, 'articles/category_detail.html', context)


def article_list_view(request):
    # Pobieramy TYLKO opublikowane artykuły
    published_articles = Article.objects.filter(is_published=True)
    
    # Obliczamy datę sprzed 3 dni
    three_days_ago = timezone.now() - timedelta(days=3)
    
    context = {
        'articles': published_articles,
        'three_days_ago': three_days_ago
    }
    return render(request, 'articles/article_list.html', context)


def article_list_view(request):
    # Najpierw pobieramy wszystkie opublikowane artykuły
    articles = Article.objects.filter(is_published=True)
    
    # Pobieramy wartość parametru 'q' z żądania GET (jeśli nie istnieje, zwróci None)
    query = request.GET.get('q')
    
    # Jeśli użytkownik coś wpisał, filtrujemy wyniki
    if query:
        # title__icontains sprawdza, czy pole title zawiera szukaną frazę (niezależnie od wielkości liter)
        articles = articles.filter(title__icontains=query)
    
    three_days_ago = timezone.now() - timedelta(days=3)
    
    context = {
        'articles': articles,
        'three_days_ago': three_days_ago,
        'search_query': query # Przekazujemy zapytanie do szablonu, aby zapamiętać wpisany tekst w polu
    }
    return render(request, 'articles/article_list.html', context)