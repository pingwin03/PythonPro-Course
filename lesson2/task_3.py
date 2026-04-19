#Prosty kalkulator obwodu: Napisz program, który poprosi użytkownika o długość i
#szerokość prostokąta, a następnie obliczy i wyświetli jego obwód (P = 2 * (długość +
#szerokość)).

długość = float(input("Podaj długość prostokąta: "))
szerokosc = float(input("Podaj szerokość protokąta: "))
odwód = 2  * (długość + szerokosc)
print("Obwód prostokąta wynosi:", odwód)