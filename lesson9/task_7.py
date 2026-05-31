# Tworzenie struktury folderów: Użyj modułu pathlib , aby napisać skrypt, który tworzy
# strukturę folderów: Projekt/src , Projekt/data , Projekt/docs 

from pathlib import Path

Path("Projekt/src").mkdir(parents=True, exist_ok=True)
Path("Projekt/data").mkdir(parents=True, exist_ok=True)
Path("Projekt/docs").mkdir(parents=True, exist_ok=True)