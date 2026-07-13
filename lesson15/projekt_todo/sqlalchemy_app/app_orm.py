# sqlalchemy_app/app_orm.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from sqlalchemy_app.database import get_db, engine
from sqlalchemy_app.models import Zadanie, Tag, Base

def pokaz_zadania(db: Session):
    """Wyświetla listę wszystkich zadań wraz z ich tagami."""
    zadania = db.query(Zadanie).all()
    if not zadania:
        print("Brak zadań na liście.")
        return
    print("\n--- Twoja lista zadań (ORM) ---")
    for zadanie in zadania:
        status = "v" if zadanie.zrobione else "x"
        # Wyciągamy nazwy tagów dla każdego zadania
        tagi_str = ", ".join([t.nazwa for t in zadanie.tagi]) if zadanie.tagi else "brak"
        print(f"[{status}] ID: {zadanie.id}, Opis: {zadanie.opis} [Tagi: {tagi_str}]")
    print("\n")

def dodaj_zadanie(db: Session, opis: str):
    """Dodaje nowe zadanie do bazy."""
    nowe_zadanie = Zadanie(opis=opis)
    db.add(nowe_zadanie)
    db.commit()
    db.refresh(nowe_zadanie)

def oznacz_jako_zrobione(db: Session, id_zadania: int):
    """Oznacza zadanie jako zrobione."""
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    if zadanie:
        zadanie.zrobione = True
        db.commit()
        print("Zadanie zaktualizowane!")
    else:
        print("Nie znaleziono zadania o podanym ID.")

def usun_zadanie(db: Session, id_zadania: int):
    """Usuwa zadanie z bazy."""
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    if zadanie:
        db.delete(zadanie)
        db.commit()
        print("Zadanie zostało usunięte!")
    else:
        print("Nie znaleziono zadania o podanym ID.")

def szukaj_zadania(db: Session, fraza: str):
    """Wyszukuje zadania po frazie."""
    zadania = db.query(Zadanie).filter(Zadanie.opis.contains(fraza)).all()
    if not zadania:
        print(f"Brak zadań pasujących do frazy: '{fraza}'")
        return
    print(f"\n--- Wyniki wyszukiwania dla: '{fraza}' ---")
    for zadanie in zadania:
        status = "v" if zadanie.zrobione else "x"
        print(f"[{status}] ID: {zadanie.id}, Opis: {zadanie.opis}")
    print("\n")

def edytuj_zadanie(db: Session, id_zadania: int):
    """Interaktywna edycja opisu zadania (Zadanie 10)."""
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    if zadanie:
        nowy_opis = input(f"Aktualny opis: '{zadanie.opis}'. Podaj nowy opis: ")
        if nowy_opis.strip():
            zadanie.opis = nowy_opis
            db.commit()
            print("Pomyślnie zaktualizowano opis zadania!")
        else:
            print("Opis nie może być pusty. Anulowano.")
    else:
        print("Nie znaleziono zadania o podanym ID.")

def dodaj_tag_do_zadania(db: Session, id_zadania: int, nazwa_tagu: str):
    """Tworzy lub wyszukuje tag i przypisuje go do zadania (Zadanie 9e)."""
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    if not zadanie:
        print("Nie znaleziono zadania o podanym ID.")
        return

    # Sprawdź czy tag już istnieje w bazie, jeśli nie - stwórz go
    tag = db.query(Tag).filter(Tag.nazwa == nazwa_tagu.lower()).first()
    if not tag:
        tag = Tag(nazwa=nazwa_tagu.lower())
        db.add(tag)
    
    # Przypisanie relacji obiektowo
    if tag not in zadanie.tagi:
        zadanie.tagi.append(tag)
        db.commit()
        print(f"Dodano tag '{nazwa_tagu}' do zadania ID {id_zadania}!")
    else:
        print("To zadanie ma już przypisany ten tag.")

def main():
    # AUTOMATYCZNE TWORZENIE TABEL
    Base.metadata.create_all(bind=engine)
    db_generator = get_db()
    db_session = next(db_generator)
    
    while True:
        print("Menu (SQLAlchemy - Pełna Wersja):")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz zadanie jako zrobione")
        print("4. Usuń zadanie")
        print("5. Wyszukaj zadanie")
        print("6. Edytuj zadanie (Zadanie 10)")
        print("7. Dodaj tag do zadania (Zadanie 9)")
        print("8. Wyjdź")
        wybor = input("Wybierz opcję: ")
        
        if wybor == '1':
            pokaz_zadania(db_session)
        elif wybor == '2':
            opis = input("Podaj opis zadania: ")
            dodaj_zadanie(db_session, opis)
            print("Zadanie dodane!")
        elif wybor == '3':
            try:
                id_zadania = int(input("Podaj ID zadania do oznaczenia: "))
                oznacz_jako_zrobione(db_session, id_zadania)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == '4':
            try:
                id_zadania = int(input("Podaj ID zadania do usunięcia: "))
                usun_zadanie(db_session, id_zadania)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == '5':
            fraza = input("Podaj szukaną frazę: ")
            szukaj_zadania(db_session, fraza)
        elif wybor == '6':
            try:
                id_zadania = int(input("Podaj ID zadania do edycji: "))
                edytuj_zadanie(db_session, id_zadania)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == '7':
            try:
                id_zadania = int(input("Podaj ID zadania: "))
                nazwa_tagu = input("Podaj nazwę tagu (np. dom, praca): ")
                dodaj_tag_do_zadania(db_session, id_zadania, nazwa_tagu)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == '8':
            print("Do zobaczenia!")
            db_session.close()
            break
        else:
            print("Nieznana opcja, spróbuj ponownie.")

if __name__ == "__main__":
    main()