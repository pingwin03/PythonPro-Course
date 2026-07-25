# cars/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Car, Dealer  # Pamiętam, żeby zaimportować też model Dealer!

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # Upewnij się, że 'photo_thumbnail' jest tutaj na liście!
    list_display = ('brand', 'model', 'photo_thumbnail', 'full_name', 'year', 'is_available')
    
    search_fields = ('brand', 'model')
    list_filter = ('is_available', 'year')
    ordering = ('-year',)
    readonly_fields = ('year',)
    actions = ['mark_as_unavailable']

    # --- Zadanie 9: Wyświetlanie miniaturki zdjęcia ---
    def photo_thumbnail(self, obj):
        if obj.photo:
            # Używam format_html, aby bezpiecznie wyświetlić obrazek
            return format_html('<img src="{}" width="150" />', obj.photo.url)
        return "Brak zdjęcia"
    
    # Ustawiam nazwę kolumny na 'Miniaturka'
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
        
        
# --- Zadanie 10: Model powiązany i Inline ---

class CarInline(admin.TabularInline):
    model = Car
    extra = 1  # Określam, ile pustych wierszy ma pokazać Django do szybkiego dodawania aut


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    inlines = [CarInline]  # Tutaj spinam model Dealera z tabelką samochodów!