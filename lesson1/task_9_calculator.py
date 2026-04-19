a = float(input("Podaj pierwszą liczbę:"))
b = float(input("Podaj drugą liczbę:"))
znak = input("Podaj działanie (+, -, *, /):")



if znak == "+":
    print("Wynik:", a + b)
elif znak ==  "-":
    print("Wynik:", a - b)
elif znak == "*":
    print("Wynmik:", a * b)
elif znak == "/":
    if b != 0:
        print("Wynik:", a / b)
    else:
        print("Nie można dzielić przez zero.")
else: 
    print("Nieznany operator.")
