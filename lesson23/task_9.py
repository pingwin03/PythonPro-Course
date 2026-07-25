# Zadanie 9 – Wyświetlanie miniaturki zdjęcia
# W widoku listy (list_display) w CarAdmin wyświetl miniaturkę zdjęcia z pola photo. Pamiętaj
# o bezpieczeństwie i użyj format_html. Ustaw szerokość obrazka na 150 pikseli.


# cars/admin.py
from django.contrib import admin
from django.utils.html import format_html  # Importuję funkcję format_html
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # Zadanie 2, 6 i 9: Dodaję 'photo_thumbnail' do listy wyświetlanych kolumn
    list_display = ('brand', 'model', 'photo_thumbnail', 'full_name', 'year', 'is_available')
    search_fields = ('brand', 'model')
    list_filter = ('is_available', 'year')
    ordering = ('-year',)
    readonly_fields = ('year',)
    actions = ['mark_as_unavailable']

    # --- Zadanie 9: Wyświetlanie miniaturki zdjęcia ---
    def photo_thumbnail(self, obj):
        # Sprawdzam, czy obiekt ma w ogóle przypisane zdjęcie
        if obj.photo:
            # Używam format_html, aby bezpiecznie wyrenderować tag <img> z szerokością 150px
            return format_html('<img src="{}" width="150" />', obj.photo.url)
        # Zwracam tekst zastępczy, jeśli zdjęcia nie ma
        return "Brak zdjęcia"
    
    # Ustawiam nagłówek kolumny
    photo_thumbnail.short_description = 'Miniaturka'

    # --- Zadanie 6: Pole generowane dynamicznie ---
    def full_name(self, obj):
        return f"{obj.brand} {obj.model}"
    
    full_name.short_description = 'Pełna nazwa'

    # --- Zadanie 8: Definicja własnej akcji ---
    @admin.action(description='Oznacz jako niedostępne')
    def mark_as_unavailable(self, request, queryset):
        updated_count = queryset.update(is_available=False)
        self.message_user(request, f'Sukces! Oznaczono {updated_count} samochodów jako niedostępne.')