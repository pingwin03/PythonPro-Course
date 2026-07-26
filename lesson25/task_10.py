# Zadanie 10 – Własna walidacja w serializatorze
# (challenge)
# W serializatorze dla notatek (z zadania 6) dodaj własną metodę walidacji (validate_title),
# która sprawdzi, czy tytuł notatki nie jest krótszy niż 5 znaków. Jeśli jest, serializator
# powinien zwrócić błąd walidacji z odpowiednim komunikatem. Przetestuj działanie, próbując
# dodać za krótką notatkę przez Postmana.


# products_app/serializers.py
from rest_framework import serializers
from .models import Product, Note, Author, Book

# ... (inne serializatory)

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
    
    
    Test Postman zrzut ekranu