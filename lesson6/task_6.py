#Wielokrotne powitanie: Napisz funkcję wielokrotne_powitanie(imie: str, ilosc:
#int) -> None , która wyświetla powitanie f"Cześć, {imie}!" tyle razy, ile wynosi
#ilosc . Ta funkcja nie powinna niczego zwracać.


def wielokrotne_powitanie(imie: str, ilosc: int) -> None:
    for i in range(ilosc):
        print(f"Cześć, {imie}!")
        
        
wielokrotne_powitanie("RAFAŁ", 3)
wielokrotne_powitanie("MAMA :)", 2)        