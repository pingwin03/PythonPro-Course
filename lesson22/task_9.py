# Zadanie 9 – Rozbudowa Seedera o Tagi
# Rozbuduj swoją komendę seed_blog. Po stworzeniu postów, skrypt powinien losowo
# przypisać od 1 do 5 istniejących tagów do każdego posta. (challenge)


# Aby dodać obsługę tagów, muszę zaktualizować  plik blog/management/commands/seed_blog.py.


import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
# Dodaję model Tag do importów
from blog.models import Post, Category, Author, Tag

class Command(BaseCommand):
    help = 'Czysci baze z postow, kategorii i tagow, a nastepnie seeduje nowymi danymi'

    def handle(self, *args, **kwargs):
        fake = Faker('pl_PL')

        self.stdout.write("Usuwanie istniejących danych...")
        
        # Na samym początku czyszczę bazę z postów, kategorii i tagów, 
        # aby mieć czystą kartę przy każdym uruchomieniu seedera
        Post.objects.all().delete()
        Category.objects.all().delete()
        Tag.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Baza wyczyszczona z postów, kategorii i tagów."))

        # Tworzę listę początkowych tagów i zapisuję je do bazy
        tag_names = ['python', 'django', 'webdev', 'programowanie', 'tutorial', 'nauka', 'lifestyle', 'tech']
        tags = []
        for name in tag_names:
            tag = Tag.objects.create(name=name)
            tags.append(tag)
        self.stdout.write(self.style.SUCCESS(f"Utworzyłem {len(tags)} tagów."))

        # Tworzę predefiniowane kategorie i zapisuję je do bazy
        category_names = ['Technologia', 'Podróże', 'Kulinaria', 'Sport', 'Gry', 'Kultura', 'Nauka']
        categories = []
        for name in category_names:
            category = Category.objects.create(name=name)
            categories.append(category)
        self.stdout.write(self.style.SUCCESS(f"Utworzyłem {len(categories)} kategorii."))

        # Pobieram istniejących autorów z bazy. Jeśli baza jest pusta, tworzę 5 nowych.
        authors = list(Author.objects.all())
        if not authors:
            for _ in range(5):
                authors.append(Author.objects.create(name=fake.name(), email=fake.email()))
            self.stdout.write(self.style.SUCCESS("Utworzyłem 5 nowych autorów, ponieważ baza była pusta."))

        self.stdout.write("Generowanie 100 losowych postów...")
        for _ in range(100):
            fake_date = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.get_current_timezone())
            
            # Zapisuję nowo utworzonego posta do zmiennej "post", 
            # ponieważ potrzebuję jego ID w bazie, by przypisać mu tagi
            post = Post.objects.create(
                title=fake.sentence(nb_words=6)[:-1], 
                content=fake.text(max_nb_chars=800),
                author=random.choice(authors),
                category=random.choice(categories),
                publication_date=fake_date
            )
            
            # Losuję liczbę od 1 do 5 - to będzie liczba tagów dla tego konkretnego posta
            k_tags = random.randint(1, min(5, len(tags)))
            
            # Używam random.sample, aby wybrać unikalne tagi z listy moich wszystkich tagów
            random_tags = random.sample(tags, k_tags)
            
            # Przypisuję wylosowane tagi do mojego posta używając wbudowanej w Django metody set()
            post.tags.set(random_tags)

        self.stdout.write(self.style.SUCCESS("Zakończone! Wygenerowałem 100 postów i każdemu przypisałem od 1 do 5 tagów."))
        
        




python manage.py seed_blog

wynik:
    (venv) PS E:\PythonPro-Course\homework\lesson22> python manage.py seed_blog
Usuwanie istniejących danych...
Baza wyczyszczona z postów, kategorii i tagów.
Utworzyłem 8 tagów.
Utworzyłem 7 kategorii.
Generowanie 100 losowych postów...
Zakończone! Wygenerowałem 100 postów i każdemu przypisałem od 1 do 5 tagów.
(venv) PS E:\PythonPro-Course\homework\lesson22> 