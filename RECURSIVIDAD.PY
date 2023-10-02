capital = int(input("Ingrese el dinero"))
T= int(input("La cantidad de años a dejar el dinero"))
In=int(input("Ingrese los intereses"))
i= int()
for i in range (T):
    capital=capital + (capital*In)/100
print("El valor total + los interes a pasar de el tiempo es ",capital)


