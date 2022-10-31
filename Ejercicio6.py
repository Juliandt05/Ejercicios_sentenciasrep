vNum=[]
contadori=0
contadorp=0

num1=int(input("Dime un número "))
num2=int(input("Dime otro número "))
for r in range (num1,num2+1):
    if r%2==0:
        contadorp+=1
    else:
        contadori+=1
print(contadorp,"Numeros pares")
print(contadori,"Numeros impares")
