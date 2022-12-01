
num_primo=0
numero=int(input("Dime un número "))
for i in range (2,numero):
    if numero%i==0:
        num_primo+=1
if num_primo>=1:
    print("El número no es primo")
else:
    print("El número es primo")
    

