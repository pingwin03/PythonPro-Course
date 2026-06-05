# Zadanie 7 – Enkapsulacja w Telewizorze
# Stwórz klasę Telewizor. Użyj enkapsulacji, aby ukryć następujące atrybuty: kanal
# (domyślnie 1), glosnosc (domyślnie 10), __wlaczony (domyślnie False). Stwórz publiczne
# metody do zarządzania telewizorem:
# wlacz() i wylacz()
# zmien_kanal(numer) : kanał można zmienić tylko, gdy TV jest włączony.
# glosniej() i ciszej() : głośność można regulować w zakresie 0-100 i tylko, gdy TV
# jest włączony.
# info(): wyświetla aktualny stan (włączony/wyłączony, kanał, głośność). Przetestuj, czy
# nie da się zmienić kanału na wyłączonym telewizorze lub ustawić głośności powyżej
# 100.




class Telewizor:
    def __init__(self):
        self.__kanal = 1
        self.__glosnosc = 10
        self.__wlaczony = False

    def wlacz(self):
        if self.__wlaczony:
            print("Telewizor jest już włączony.")
        else:
            self.__wlaczony = True
            print("Telewizor włączony.")

    def wylacz(self):
        if not self.__wlaczony:
            print("Telewizor jest już wyłączony.")
        else:
            self.__wlaczony = False
            print("Telewizor wyłączony.")

    def zmien_kanal(self, numer):
        if not self.__wlaczony:
            print("Nie można zmienić kanału – telewizor jest wyłączony.")
        else:
            self.__kanal = numer
            print(f"Zmieniono kanał na {self.__kanal}.")

    def glosniej(self, wartosc=10):
        if not self.__wlaczony:
            print("Nie można zmienić głośności – telewizor jest wyłączony.")
        elif self.__glosnosc + wartosc > 100:
            print(f"Maksymalna głośność to 100. Aktualna głośność: {self.__glosnosc}.")
        else:
            self.__glosnosc += wartosc
            print(f"Głośność zwiększona do {self.__glosnosc}.")

    def ciszej(self, wartosc=10):
        if not self.__wlaczony:
            print("Nie można zmienić głośności – telewizor jest wyłączony.")
        elif self.__glosnosc - wartosc < 0:
            print(f"Minimalna głośność to 0. Aktualna głośność: {self.__glosnosc}.")
        else:
            self.__glosnosc -= wartosc
            print(f"Głośność zmniejszona do {self.__glosnosc}.")

    def info(self):
        stan = "włączony" if self.__wlaczony else "wyłączony"
        print(f"Stan: {stan} | Kanał: {self.__kanal} | Głośność: {self.__glosnosc}/100")


# ── Testy ──────────────────────────────────────────────
tv = Telewizor()

print("=== Stan początkowy ===")
tv.info()

print("\n=== Próby na wyłączonym TV ===")
tv.zmien_kanal(5)
tv.glosniej()

print("\n=== Włączamy TV ===")
tv.wlacz()
tv.info()

print("\n=== Normalne operacje ===")
tv.zmien_kanal(13)
tv.glosniej()
tv.glosniej()
tv.ciszej(5)
tv.info()

print("\n=== Próba przekroczenia limitu głośności ===")
tv.glosniej(99)

print("\n=== Próba zejścia poniżej 0 ===")
tv.ciszej(99)

print("\n=== Wyłączamy TV ===")
tv.wylacz()
tv.info()