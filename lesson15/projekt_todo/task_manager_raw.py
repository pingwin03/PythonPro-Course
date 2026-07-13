import sqlite3

class TaskManagerRaw:
    def __init__(self, db_name='todo_raw.db'):
        self.db_name = db_name
        self.init_db()

    def _execute_query(self, query: str, params: tuple = (), fetch=False):
        """Pomocnicza metoda do współdzielenia połączenia SQL."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            if fetch:
                return cursor.fetchall()
            conn.commit()

    def init_db(self):
        self._execute_query('''
            CREATE TABLE IF NOT EXISTS zadania (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                opis TEXT NOT NULL,
                zrobione BOOLEAN NOT NULL CHECK (zrobione IN (0,1))
            )
        ''')

    def dodaj(self, opis: str):
        self._execute_query("INSERT INTO zadania (opis, zrobione) VALUES (?, ?)", (opis, False))

    def pobierz_wszystkie(self):
        return self._execute_query("SELECT id, opis, zrobione FROM zadania", fetch=True)

    def oznacz_jako_zrobione(self, id_zadania: int):
        self._execute_query("UPDATE zadania SET zrobione = ? WHERE id = ?", (True, id_zadania))

    def usun(self, id_zadania: int):
        self._execute_query("DELETE FROM zadania WHERE id = ?", (id_zadania,))

    def szukaj(self, fraza: str):
        return self._execute_query("SELECT id, opis, zrobione FROM zadania WHERE opis LIKE ?", (f"%{fraza}%",), fetch=True)


# Prosty skrypt uruchamiający klasę w konsoli
if __name__ == "__main__":
    manager = TaskManagerRaw()
    while True:
        print("\n--- Menu Klasowe (Raw SQL) ---")
        print("1. Pokaż | 2. Dodaj | 3. Zrób | 4. Usuń | 5. Szukaj | 6. Wyjdź")
        wybor = input("Wybierz: ")
        
        if wybor == '1':
            for z in manager.pobierz_wszystkie():
                print(f"[{'v' if z[2] else 'x'}] ID: {z[0]} | {z[1]}")
        elif wybor == '2':
            manager.dodaj(input("Opis: "))
        elif wybor == '3':
            manager.oznacz_jako_zrobione(int(input("ID: ")))
        elif wybor == '4':
            manager.usun(int(input("ID do usunięcia: ")))
        elif wybor == '5':
            for z in manager.szukaj(input("Szukaj frazy: ")):
                print(f"[{'v' if z[2] else 'x'}] ID: {z[0]} | {z[1]}")
        elif wybor == '6':
            break