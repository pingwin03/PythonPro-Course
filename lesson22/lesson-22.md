Poniżej masz **oczyszczoną i poprawioną wersję**.
Usunąłem chaos, poprawiłem spójność i dodałem **krótkie, sensowne komentarze w kodzie (bez lania wody)**.

---

# **Lekcja 22: Zaawansowana Praca z Bazą Danych w Django**

`#lekcja` `#python` `#django` `#orm` `#bazydanych` `#queryset` `#faker`

W tej lekcji skupiamy się na 4 kluczowych elementach Django ORM:

* modele
* relacje
* filtrowanie (w tym po relacjach)
* walidacja (validators / clean / full_clean / save)

---

# 1. Modele — struktura danych

Model = tabela w bazie danych.

```python id="m1"
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
```

```python id="m2"
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
```

---

# 2. Relacje między tabelami

## 2.1 One-to-many (ForeignKey)

```python id="r1"
class Post(models.Model):
    # każdy post ma jednego autora, autor ma wiele postów
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

---

## 2.2 One-to-one

```python id="r2"
class Profile(models.Model):
    # jeden użytkownik → jeden profil
    user = models.OneToOneField(User, on_delete=models.CASCADE)
```

---

## 2.3 Many-to-many

```python id="r3"
class Post(models.Model):
    # post może mieć wiele tagów, tag może być w wielu postach
    tags = models.ManyToManyField("Tag")
```

---

## 2.4 Tworzenie relacji w praktyce

```python id="r4"
author = Author.objects.create(name="Jan")

# przypisanie relacji FK przy tworzeniu obiektu
post = Post.objects.create(title="Test", author=author)
```

---

# 3. QuerySet i filtrowanie

## 3.1 Podstawowe filtrowanie

```python id="q1"
Post.objects.filter(title="Django")
```

---

## 3.2 Lookupy (operatory)

```python id="q2"
# dokładne dopasowanie (domyślne)
title__exact="Django"

# fragment tekstu
title__contains="Django"

# case-insensitive
title__icontains="django"

# lista wartości
id__in=[1, 2, 3]

# porównania liczbowe
age__gt=18
```

---

## 3.3 Filtrowanie po relacjach (JOIN)

```python id="q3"
# JOIN: Post → Author
Post.objects.filter(author__name="Jan")
```

```python id="q4"
# JOIN: Post → Tags (M2M)
Post.objects.filter(tags__name__icontains="py")
```

```python id="q5"
# wielopoziomowe JOIN-y
Post.objects.filter(author__profile__city="Gliwice")
```

---

## 3.4 DISTINCT (ważne przy M2M)

```python id="q6"
# usuwa duplikaty wynikające z JOIN ManyToMany
Post.objects.filter(tags__name__icontains="py").distinct()
```

---

# 4. Walidacja w Django ORM

## 4.1 Validators (pojedyncze pole)

```python id="v1"
def validate_even(value):
    # walidacja jednego pola
    if value % 2 != 0:
        raise ValidationError("Musi być parzyste")
```

---

## 4.2 clean() — walidacja modelu

```python id="v2"
def clean(self):
    # logika między polami modelu
    if self.start > self.end:
        raise ValidationError("Błędny zakres")
```

---

## 4.3 full_clean()

```python id="v3"
obj.full_clean()
```

Uruchamia:

* validators pól
* clean_fields()
* clean()
* validate_unique()

---

## 4.4 save()

```python id="v4"
obj.save()
# zapis do bazy
# NIE odpala automatycznie full_clean()
```

---

## 4.5 Model walidacji (mental model)

* validators → pojedyncze pole
* clean() → logika modelu
* full_clean() → pełna walidacja
* save() → zapis do DB

---

# 5. ORM lifecycle (skrót)

```text id="l1"
create object
→ (full_clean opcjonalnie)
→ pre_save
→ save()
→ post_save
```

---

# 6. Django vs Flask (SQLAlchemy)

## Django ORM

* wysoki poziom abstrakcji
* deklaratywne modele
* automatyczne relacje
* QuerySet + lookup system

## Flask + SQLAlchemy

* niższy poziom
* jawne session management
* większa kontrola SQL
* więcej kodu

---

| Django        | Flask              |
| ------------- | ------------------ |
| prostota      | kontrola           |
| automatyzacja | jawność            |
| ORM lifecycle | session-based flow |

---

# 7. Seeder / Faker

```python id="s1"
fake = Faker("pl_PL")  # generator realistycznych danych PL
```

---

# 8. Najważniejsze idee

## Modele

* struktura bazy danych

## Relacje

* ForeignKey / OneToOne / ManyToMany
* JOIN-y przez `__`

## QuerySet

* lazy evaluation
* lookup system (`contains`, `icontains`, `gt`, `in`)

## Walidacja

* validators (field)
* clean (model)
* full_clean (pipeline)
* save (persist)

---

# 9. Podsumowanie

Django ORM łączy modele, relacje i walidację w jeden system, gdzie:

* dane są deklaratywne
* zapytania budowane przez lookupi
* walidacja działa warstwowo
* zapis kontroluje lifecycle ORM

---

# 🧪 Zadania do samodzielnej pracy

(zostawione bez zmian)

---

Jeśli chcesz, mogę zrobić z tego **wersję “1 strona A4 cheat sheet” albo wersję pod rozmowę rekrutacyjną (ultra skrót)**.
