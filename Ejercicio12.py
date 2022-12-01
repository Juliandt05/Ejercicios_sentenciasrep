mesahorro=[]
ahorrofinal=0

for i in range(1,13):
    aho=(int(input("Cuanto has ahorrado este mes?\n")))
    mesahorro.append(aho)
    ahorrofinal=aho+ahorrofinal
print("En total su ahorro es de",ahorrofinal)
num_mes=int(input("Dime un mes empezando Enero por el 0 y Diciembre el 11:\n"))
print("En ese mes usted ahorró",mesahorro[num_mes])
sumatoria_mes=0
for  z in range(num_mes+1):
    sumatoria_mes+=mesahorro[z]
print("En este mes ahorraste",sumatoria_mes,"€ en total")
