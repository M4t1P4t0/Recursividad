n1=1
n2=0
n=n1+(2*n2)
cont=0
    
while n<300:
    n2=n1
    n1=n
    n=n1+(2*n2)
    cont=cont+1 
     
print(" su rango es ",cont," y su resultad0o es ",n)    