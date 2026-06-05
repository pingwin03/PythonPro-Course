#Zen w częściach: Wyświetl na ekranie tylko pierwsze dwie linijki z "Zenu Pythona".
#Wskazówka: musisz pobrać cały tekst i przetworzyć go jako ciąg znaków lub listę.

import io
import sys

# Przechwytujemy stdout, bo import this od razu drukuje tekst
bufor = io.StringIO()
stary_stdout = sys.stdout
sys.stdout = bufor

import this

sys.stdout = stary_stdout

# Pobieramy cały tekst i dzielimy na linie
tekst = bufor.getvalue()
linie = tekst.splitlines()

# Wyświetlamy tylko pierwsze dwie niepuste linie
pierwsze_dwie = [linia for linia in linie if linia.strip()][:2]
for linia in pierwsze_dwie:
    print(linia)                        