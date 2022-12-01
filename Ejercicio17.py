trab=int(input("Dime la cantidad de empleados que tienes: "))
suelh=int(input("Dime cuanto cobran a la hora: "))
horastot=0
for i in range(1,trab+1):
    diast = int(input("Dime la cantidad de días que has trabajado: "))
    for a in range(1, diast + 1):
        horastrab = int(input("Dime las horas que has trabajado  en este día: "))
        horastot += horastrab
    print("Este trabajador cobrará:", horastot*suelh)