# =========================================================================
# PLIK: app.py - Szkielet bazowy dla aplikacji Flask i bazy danych
# =========================================================================
# Przed uruchomieniem upewnij się, że zainstalowałeś biblioteki poleceniem:
# pip install Flask Flask-SQLAlchemy psycopg2-binary
# =========================================================================

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Konfiguracja połączenia z PostgreSQL (zmień dane na swoje dane lokalne)
# Format: postgresql://uzytkownik:haslo@host:port/nazwa_bazy

# NA potrezby wykonania zadania bez konfiguracji na potrzeby wykonania zadania wykonałem projekt na SQLite 

# Zamiast wersji z postgresql://... wklej poniższą linię:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baza_projektu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicjalizacja ORM SQLAlchemy
db = SQLAlchemy(app)

# -------------------------------------------------------------------------
# MODELE BAZY DANYCH (SQLAlchemy)
# -------------------------------------------------------------------------

# Model do Zadania 8 i Zadania 9
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Model do Zadania 10
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Registration {self.email}>'

# Automatyczne tworzenie tabel w bazie przy starcie aplikacji
with app.app_context():
    db.create_all()


# REJESTRACJA ŚCIEŻEK (ROUTING) 


# Strona główna testowa
@app.route('/')
def index():
    return 'Serwer Flask działa poprawnie! Baza danych została zainicjalizowana.'

# Uzupełniony endpoint dla Zadania 1
@app.route('/me')
def me():
    # Funkcja zwraca Twoje imię i nazwisko bezpośrednio jako ciąg znaków (HTML/tekst)
    return 'Rafał Duchna'

# Uzupełniony endpoint dla Zadania 2 z dynamicznym routingiem
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    # Pobieramy liczby z adresu URL, sumujemy je i zwracamy sformatowany wynik
    suma = num1 + num2
    return f'Wynik to: {suma}'

# Uzupełniony endpoint dla Zadań 3, 4 i 5
@app.route('/movies')
def movies_list():
    # Zadanie 3: Tworzymy listę ulubionych filmów
    fav_movies = ['Incepcja', 'Władca Pierścieni', 'Matrix', 'Interstellar']
    
    # Zadanie 4: Przekazujemy listę oraz zmienną page_title z dynamicznym tytułem strony do szablonu
    return render_template('movies.html', page_title="Moje ulubione filmy", movies=fav_movies)

# Uzupełniony endpoint dla Zadania 6
@app.route('/book')
def show_book():
    # Tworzymy słownik opisujący książkę zgodnie z treścią zadania
    book_data = {
        'title': 'Hobbit',
        'author': 'J.R.R. Tolkien',
        'year': 1937
    }
    # Przekazujemy słownik do szablonu pod nazwą 'book'
    return render_template('book.html', book=book_data)

# Uzupełniony endpoint dla Zadania 7
@app.route('/gallery')
def show_gallery():
    # Lista słowników z przykładowymi obrazkami i ich podpisami
    images_list = [
        {'url': 'https://picsum.photos/id/10/300/200', 'caption': 'Góry i las'},
        {'url': 'https://picsum.photos/id/20/300/200', 'caption': 'Stary aparat'},
        {'url': 'https://picsum.photos/id/29/300/200', 'caption': 'Górski szczyt'}
    ]
    # Przekazujemy listę do szablonu gallery.html
    return render_template('gallery.html', gallery=images_list)

# Uzupełniony endpoint dla Zadania 8 i Zadania 9
@app.route('/products')
def list_products():
    # Zadanie 8 (Automatyczne zasilenie bazy danych, jeśli jest pusta)
    # Sprawdzamy, czy w bazie są już jakieś produkty, żeby nie dodawać ich w nieskończoność przy każdym odświeżeniu
    if Product.query.count() == 0:
        p1 = Product(name="Myszka bezprzewodowa", price=89.99)
        p2 = Product(name="Klawiatura mechaniczna", price=249.50)
        p3 = Product(name="Monitor 24 cale", price=599.00)
        
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.commit() # Zatwierdzamy zmiany w bazie danych

    # Zadanie 9: Pobieramy wszystkie produkty z bazy (odpowiednik SELECT * FROM product;)
    all_products = Product.query.all()
    
    # Przekazujemy listę obiektów produktów do szablonu HTML
    return render_template('products.html', products=all_products)

# Uzupełniony endpoint dla Zadania 10 (Obsługa GET i POST)
@app.route('/register', methods=['GET', 'POST'])
def register():
    # d. Sprawdzamy, czy użytkownik kliknął przycisk i przesłał formularz (POST)
    if request.method == 'POST':
        # Pobieramy dane wpisane przez użytkownika w pola formularza na podstawie atrybutu 'name' w HTML
        u_name = request.form.get('name')
        u_email = request.form.get('email')
        
        # Tworzymy nowy obiekt rejestracji
        new_reg = Registration(name=u_name, email=u_email)
        
        try:
            db.session.add(new_reg) # Dodajemy do sesji bazy
            db.session.commit()    # Zapisujemy w pliku bazy danych
            # Po poprawnym zapisie przekierowujemy użytkownika na stronę z podziękowaniem
            return redirect(url_for('thank_you'))
        except Exception:
            db.session.rollback() # W razie błędu wycofujemy operację
            return "<h3>Błąd: Ten adres e-mail został już zarejestrowany!</h3>"

    # Jeśli użytkownik po prostu wchodzi na stronę (GET), wyświetlamy mu pusty formularz
    return render_template('register.html')

@app.route('/thank-you')
def thank_you():
    return '<h1>Dziękujemy za rejestrację!</h1>'

# Uruchomienie aplikacji w trybie debugowania
if __name__ == '__main__':
    app.run(debug=True)