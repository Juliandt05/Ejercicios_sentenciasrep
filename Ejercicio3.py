num=1
suma=0
elementos=0
while num!=0:
    num=int(input("Dime un número "))
    suma=suma+num
    elementos=elementos+1
print("La suma es",suma)
print("La media es",suma/(elementos-1))