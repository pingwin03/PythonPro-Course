# Zadanie 8 – Własna akcja
# Stwórz niestandardową akcję (Admin Action) o nazwie "Oznacz jako niedostępne"
# (mark_as_unavailable), która dla zaznaczonych samochodów ustawi pole is_available na
# False. Nie zapomnij o komunikacie dla użytkownika



# cars/admin.py
from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'full_name', 'year', 'is_available')
    search_fields = ('brand', 'model')
    list_filter = ('is_available', 'year')
    ordering = ('-year',)
    readonly_fields = ('year',)

    # --- Zadanie 8: Rejestracja własnej akcji ---
    # Dodaję moją nową metodę do listy dostępnych akcji
    actions = ['mark_as_unavailable']

    # --- Zadanie 6: Pole generowane dynamicznie ---
    def full_name(self, obj):
        return f"{obj.brand} {obj.model}"
    
    full_name.short_description = 'Pełna nazwa'

    # --- Zadanie 8: Definicja własnej akcji ---
    @admin.action(description='Oznacz jako niedostępne')
    def mark_as_unavailable(self, request, queryset):
        # Aktualizuję pole is_available na False dla wszystkich zaznaczonych elementów
        updated_count = queryset.update(is_available=False)
        
        # Wyświetlam komunikat dla użytkownika w panelu
        self.message_user(request, f'Sukces! Oznaczono {updated_count} samochodów jako niedostępne.')