
numero=int(input("Dime el número al que le quieres hacer el factorial"))
resultado=1

for num in range (1,numero+1):
    resultado=resultado*num
print("El factorial de",num,"es",resultado)


