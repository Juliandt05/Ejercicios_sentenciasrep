
base=int(input("Dime la base de la potencia"))
poten=base
expo=int(input("Dime el exponente de la potencia"))

for i in range(expo-1):
    poten*= base
print(poten)