salida=-1
base=int(input("Dime la base de la potencia"))
poten=base
expo=int(input("Dime el exponente de la potencia"))

for i in range(expo):
    poten=poten*base


print(base)