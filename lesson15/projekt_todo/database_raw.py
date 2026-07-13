# database_raw.py
import sqlite3

DATABASE_NAME = 'todo_raw.db'

def init_db():
    """Inicjalizuje bazę danych i tworzy tabelę, jeśli nie istnieje."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        # Używamy IF NOT EXISTS, aby uniknąć błędu przy ponownym uruchomieniu
        # Zadanie 4 – Dodanie priorytetu (Raw SQL)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS zadania (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                opis TEXT NOT NULL,
                zrobione BOOLEAN NOT NULL CHECK (zrobione IN (0,1)),
                priorytet INTEGER DEFAULT 1  -- <--- Nowa kolumna    
             )   
        ''')
        conn.commit()
# Zadanie 4 – Dodanie priorytetu (Raw SQL)
def dodaj_zadanie(opis: str, priorytet: int = 1):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO zadania (opis, zrobione, priorytet) VALUES (?, ?, ?)", 
            (opis, False, priorytet)
        )
        conn.commit()

def pobierz_zadania():
    """Pobiera wszystkie zadania z bazy danych."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, opis, zrobione FROM zadania")
        return cursor.fetchall()

def oznacz_jako_zrobione(id_zadania: int):
    """Oznacza zadanie o podanym ID jako zrobione."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE zadania SET zrobione = ? WHERE id = ?", (True, id_zadania))
        conn.commit()
        
# Zadanie 1 – Usuwanie zadań (Raw SQL)
# Dodaj do aplikacji app_raw_sql.py opcję menu "Usuń zadanie". Zaimplementuj funkcję
# usun_zadanie(id_zadania) w database_raw.py, która użyje zapytania DELETE FROM
# zadania WHERE id = ?    

def usun_zadanie(id_zadania: int):
    """Usuwa zadanie o podanym ID z bazy danych."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM zadania WHERE id = ?", (id_zadania,))
        conn.commit()
  
# Zadanie 6 – Wyszukiwanie po opisie (Raw SQL)
# Dodaj do aplikacji app_raw_sql.py funkcję wyszukiwania zadań. Użytkownik podaje frazę, a
# program wyświetla wszystkie zadania, których opis zawiera tę frazę. Użyj operatora LIKE i
# wzorca %fraza% w zapytaniu SELECT.  
        
def szukaj_zadania(fraza: str):
    """Wyszukuje zadania, których opis zawiera podaną frazę."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        # %fraza% szuka tekstu w dowolnym miejscu kolumny 'opis'
        cursor.execute("SELECT id, opis, zrobione FROM zadania WHERE opis LIKE ?", (f"%{fraza}%",))
        return cursor.fetchall()