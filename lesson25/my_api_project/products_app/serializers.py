
from rest_framework import serializers
from .models import Product, Note, Author, Book # Importuję nowe modele

# Tworzę mój serializator, który dziedziczy po ModelSerializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        # Wskazuję, który z moich modeli ma być serializowany
        model = Product
        
        # Wymieniam w liście pola, które chcę uwzględnić, wliczając w to automatyczne 'id'
        fields = ['id', 'name', 'price']
        
        
        
# Tworzę serializator dla notatek
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at']
        
    # Tworzę własną metodę walidacji dla pola 'title'
    def validate_title(self, value):
        # Sprawdzam, czy długość przekazanego tytułu (value) jest mniejsza niż 5 znaków
        if len(value) < 5:
            # Jeśli tak, zgłaszam błąd walidacji z odpowiednim komunikatem
            raise serializers.ValidationError("Tytuł notatki musi mieć co najmniej 5 znaków.")
        
        # Jeśli wszystko jest w porządku, zwracam poprawną wartość
        return value
        
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    # Wykorzystuję StringRelatedField, aby pobrać wartość z metody __str__ modelu Author
    # Ustawiam source='author', aby DRF wiedział, skąd wziąć dane
    author_name = serializers.StringRelatedField(source='author', read_only=True)

    class Meta:
        model = Book
        # Dodaję zarówno 'author' (do obsługi ID), jak i 'author_name' (do wyświetlania nazwy)
        fields = ['id', 'title', 'publication_year', 'author', 'author_name']