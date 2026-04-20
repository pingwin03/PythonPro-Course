#Tabela mnożenia: Napisz program, który używając zagnieżdżonych pętli for (jedna w
#drugiej), wyświetli tabliczkę mnożenia od 1 do 5. (Wskazówka: for i in range(1, 6):
#for j in range(1, 6): ... )

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}", end="\t")
    print()