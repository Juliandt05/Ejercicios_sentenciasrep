totalpago = 10
Vmes = []
for i in range(1,21):
    totalpago = totalpago*2
    Vmes.append(totalpago)
print("En total pagastes", totalpago)
print("Dime en que mes")
x = int(input())
print("En ese mes pagastes", Vmes[x-1])