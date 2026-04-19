#Wyrażenie logiczne: Napisz program, który pyta, czy użytkownik ma prawo jazdy
#( tak/nie ) i ile ma lat. Wyświetl True , jeśli użytkownik ma 18 lat lub więcej ORAZ ma
#prawo jazdy. W przeciwnym razie wyświetl False .

prawko =  input("Czy masz prawo jazdy? (TAK/NIE): ")
wiek = int(input("Ile masz lat? "))

wynik = (wiek >=18) and (prawko == "tak")

print(wynik)