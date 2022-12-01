num1=0
num2=-1
numfuera=0
numinter=0
numero=int
suma=0
listasuma=[]

while num1>num2:
    try:
        print("El limite menor no puede ser mas grade que el mayor")
        num1=int(input("Dime el limete inferior "))
        num2=int(input("Dime el limite superior "))
    except:
        print("Tienes que introducir un número")

while numero!=0:
    numero=int(input("Dime un número y si introduces 0 acaba"))
    if numero>num1 and numero<num2:
        listasuma.append(numero)
    elif numero<num1 or numero>num2:
        numfuera+=1
    else:
        numinter+=1

for x in listasuma:
    suma=suma+x

print("La suma de los números introducidos que estan dentro del intervalo es",suma)
print("Hay",numfuera,"numeros fuera del intervalo")
print("De los números fuera del intervalo hay",numinter,"iguales a los limites")