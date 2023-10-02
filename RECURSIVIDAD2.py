num=int(input("Ingrese un numero, y para terminar el programa uno negativo "))
acu=int()
i=int()

if num>0:
    for i in range (num):
        i=i+1
        if num %i==0:
            acu=acu+i

print("La suma de los divisores es ",acu)