#Mini-projekt "Konwerter Temperatury": Napisz program, który poprosi użytkownika o
#temperaturę w stopniach Celsjusza, przekonwertuje ją na stopnie Fahrenheita według
#wzoru F = C * 9/5 + 32 i wyświetli wynik z wyjaśnieniem.

celsius = float(input("Podaj temperaaturę w stopniach Celsjusza: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"Temperatura {celsius} C to {fahrenheit}F.")