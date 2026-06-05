# Zadanie 4 – Czytelny Punkt
# Stwórz klasę Punkt do reprezentowania punktu w 2D, z atrybutami x i y. Zaimplementuj
# metodę str, aby print(punkt) wyświetlał współrzędne w formacie (x, y).


class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


# Tworzymy kilka punktów i drukujemy je
p1 = Punkt(3, 7)
p2 = Punkt(-1, 4)
p3 = Punkt(0, 0)

print(p1)
print(p2)
print(p3)