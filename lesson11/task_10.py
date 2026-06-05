# Zadanie 10 – Eksploracja MRO
# Stwórz następującą, złożoną hierarchię dziedziczenia:
# class A
# class B(A)
# class C(A)
# class D(B)
# class E(C)
# class F(D, E) Narysuj schemat tej hierarchii w mermaid. Następnie, nie uruchamiając
# kodu, spróbuj przewidzieć, jakie będzie MRO dla klasy F. Na koniec sprawdź swoją
# odpowiedź, używając print(F.mro()).

class A: pass
class B(A): pass
class C(A): pass
class D(B): pass
class E(C): pass
class F(D, E): pass

# Przewidywane MRO dla F (algorytm C3 linearization):
# 1. Zaczynamy od F
# 2. D jest przed E (kolejność w definicji F)
# 3. B jest rodzicem D
# 4. E jest za D, C jest rodzicem E
# 5. A pojawia się po wszystkich swoich dzieciach (B, C)
# 6. Na końcu object (każda klasa dziedziczy po object)
#
# Przewidywany wynik: [F, D, B, E, C, A, object]

print("=== Przewidywane MRO ===")
print("[F, D, B, E, C, A, object]")

print("\n=== Rzeczywiste MRO ===")
print([klasa.__name__ for klasa in F.mro()])

print("\n=== Wynik zgodny z przewidywaniem? ===")
przewidywane = [F, D, B, E, C, A, object]
print("TAK" if F.mro() == przewidywane else "NIE")