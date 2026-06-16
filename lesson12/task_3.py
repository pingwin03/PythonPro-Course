# Zadanie 3 – Konwerter Walut
# Stwórz klasę KalkulatorWalut. Dodaj w niej metodę statyczną (@staticmethod) o nazwie
# usd_na_pln, która przyjmuje kwotę w dolarach i zwraca ją przeliczoną na złotówki (przyjmij
# stały kurs, np. 1 USD = 4.0 PLN). Wywołaj tę metodę bez tworzenia obiektu klasy.



class KalkulatorWalut:
    KURS_USD_DO_PLN = 4.0

    @staticmethod
    def usd_na_pln(kwota_usd):
        return kwota_usd * KalkulatorWalut.KURS_USD_DO_PLN


# Wywołanie metody statycznej BEZ tworzenia obiektu
kwota_usd = 57
kwota_pln = KalkulatorWalut.usd_na_pln(kwota_usd)

print(f"{kwota_usd} USD = {kwota_pln} PLN")