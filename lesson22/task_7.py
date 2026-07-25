# Zadanie 7 – Seeder dla Kategorii i Postów
# Stwórz własną komendę manage.py o nazwie seed_blog. Komenda powinna:
# a. Usunąć wszystkie istniejące posty i kategorie.
# b. Stworzyć 5-10 predefiniowanych kategorii (np. "Technologia", "Podróże", "Kulinaria").
# c. Stworzyć 100 losowych postów za pomocą Faker i losowo przypisać każdy z nich do
# jednej z nowo utworzonych kategorii. (challenge)


# tworzymy"
blog/
    management/
        __init__.py
        commands/
            __init__.py
            seed_blog.py   <-- ten plik tworzę
            
            
# do - seed_blog.py

import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from blog.models import Post, Category, Author

class Command(BaseCommand):
    help = 'Czysci baze z postow i kategorii, a nastepnie seeduje nowymi danymi'

    def handle(self, *args, **kwargs):
        fake = Faker('pl_PL')

        self.stdout.write("Usuwanie istniejących postów i kategorii...")
        # a. Usunięcie wszystkich postów i kategorii
        Post.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Baza wyczyszczona z postów i kategorii."))

        # b. Stworzenie predefiniowanych kategorii
        category_names = ['Technologia', 'Podróże', 'Kulinaria', 'Sport', 'Gry', 'Kultura', 'Nauka']
        categories = []
        
        for name in category_names:
            category = Category.objects.create(name=name)
            categories.append(category)
            
        self.stdout.write(self.style.SUCCESS(f"Utworzono {len(categories)} kategorii."))

        # Zabezpieczenie: Pobieram istniejących autorów lub tworzę kilku, by móc przypisać do nich posty
        authors = list(Author.objects.all())
        if not authors:
            for _ in range(5):
                authors.append(Author.objects.create(name=fake.name(), email=fake.email()))
            self.stdout.write(self.style.SUCCESS("Utworzono 5 nowych autorów (baza autorów była pusta)."))

        # c. Stworzenie 100 losowych postów
        self.stdout.write("Generowanie 100 losowych postów...")
        for _ in range(100):
            # Używam timezone.now() by zachować zgodność z ustawieniami stref czasowych Django
            fake_date = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.get_current_timezone())
            
            Post.objects.create(
                title=fake.sentence(nb_words=6)[:-1], # [:-1] usuwa kropkę na końcu zdania z tytułu
                content=fake.text(max_nb_chars=800),
                author=random.choice(authors),
                category=random.choice(categories),
                publication_date=fake_date
            )

        self.stdout.write(self.style.SUCCESS("Zakończono! Wygenerowano i przypisano 100 postów."))
        
        
        
        
        
# python manage.py seed_blog




# wynik:
    
# (venv) PS E:\PythonPro-Course\homework\lesson22> python manage.py seed_blog
# Usuwanie istniejących postów i kategorii...
# Baza wyczyszczona z postów i kategorii.
# Utworzono 7 kategorii.
# Generowanie 100 losowych postów...
# Zakończono! Wygenerowano i przypisano 100 postów.
# (venv) PS E:\PythonPro-Course\homework\lesson22> 