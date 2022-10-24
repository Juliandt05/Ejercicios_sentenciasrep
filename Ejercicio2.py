import random

num=0
numale=random.randint(1,100)
intentos=0
print(numale)
while intentos<=10 or numale!=num or salida==1:
    num=int(input("Dime el numero secreto"))
    if num!=numale and num>numale:
        intentos=intentos+1
        print("El número es menor")
    if num!=numale and num<numale:
        intentos=intentos+1
        print("El número es mayor")
    if num==numale:
        salida=1

print("Has adivinado el número en",intentos)