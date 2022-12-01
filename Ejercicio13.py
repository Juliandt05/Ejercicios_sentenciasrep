horastot=0
for x in range (1,7):
    horas_dia=int(input("Dime las horas que has trabajado en el dia: "))
    horastot=horastot+horas_dia
sueldohora=int(input("Dime lo que cobras por hora: "))
print("Tu sueldo total es de",sueldohora*horastot)