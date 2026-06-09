# Identyfikator obiektu: Utwórz trzy zmienne ( a , b , c ) z tą samą wartością 256 . Sprawdź
# i wyświetl ich id() . Następnie utwórz trzy zmienne z wartością 257 i również sprawdź ich
# id() . Czy widzisz różnicę w zachowaniu Pythona? Wyjaśnij dlaczego w komentarzu.


# Zmienne z wartością 256
a = 256
b = 256
c = 256

print("id() dla 256:")
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
print(f"id(c) = {id(c)}")

# Zmienne z wartością 257
x = 257
y = 257
z = 257

print("\nid() dla 257:")
print(f"id(x) = {id(x)}")
print(f"id(y) = {id(y)}")
print(f"id(z) = {id(z)}")

# Wyjaśnienie
# Python optymalizuje pamięć dla małych liczb całkowitych (w tym zakresie) poprzez
# tworzenie jednego wspólnego obiektu. Liczby -5 do 256 są często "międzyniewymi"
# (interned), więc różne zmienne o tej samej wartości wskazują na TEN SAM obiekt
# w pamięci i mają IDENTYFIKATOR id().
# Dla liczb większych niż 256 (np. 257) Python nie stosuje tej optymalizacji,
# więc każda nowa przypisana wartość tworzy NOWY obiekt, co oznacza różne id().
