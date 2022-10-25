import random

num=0
numale=random.randint(1,100)
intentos=0
print(numale)
while intentos<=9 and numale!=num :
    num=int(input("Dime el numero secreto"))
    if num!=numale and num>numale:
        intentos+=1
        print("El número es menor")
    if num!=numale and num<numale:
        intentos+=1
        print("El número es mayor")
    if intentos==10:
        print("Has excedido el número máximo de intentos")
if num==numale:
    salida=1
    print("Has adivinado el número en",intentos,"intentos")

