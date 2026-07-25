import random
from django.core.management.base import BaseCommand
from faker import Faker
from blog.models import Author, Post

class Command(BaseCommand):
    help = 'Seeds the database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')
        
        # Inicjalizujemy Faker z polskim wariantem
        fake = Faker('pl_PL')
        
        # Tworzymy 10 autorów
        authors = []
        for _ in range(10):
            author = Author.objects.create(
                name=fake.name(),
                email=fake.email()
            )
            authors.append(author)
            
        self.stdout.write(self.style.SUCCESS(f'{len(authors)} authors created.'))
        
        # Tworzymy 50 postów
        posts = []
        for _ in range(50):
            post = Post.objects.create(
                title=fake.sentence(nb_words=6),
                content=' '.join(fake.paragraphs(nb=5)),
                author=random.choice(authors), # Losowy autor z listy
                publication_date=fake.date_time_this_year()
            )
            posts.append(post)
            
        self.stdout.write(self.style.SUCCESS(f'{len(posts)} posts created.'))
        self.stdout.write(self.style.SUCCESS('Data seeding complete.'))