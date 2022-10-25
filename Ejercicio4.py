numini=0
numini=int(input("Dime la cantidad de números que quieres introducir "))
numfin=0
num=int
menor=0
mayor=0
cero=0
while numfin!=numini:
    num=int(input("Dime los números a intorducir"))
    if num<0:
        menor+=1
    if num>0:
        mayor+=1
    if num==0:
        cero+=1
    numfin+=1
print("Has introducido",mayor,"números mayores que cero",menor,"números menores que cero y ",cero,"números iguales a cero")

