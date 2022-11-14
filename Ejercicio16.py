horastot = 0
print("Cuantos trabajadores tienes")
tra = int(input())
print("Cuanto cobras por hora")
dinero = int(input())
for x in range(1,7):
    print("Cuántas horas has trabajado")
    horas = int(input())
    horastotales = horas + horastotales
print("El sueldo de los", tra,"son de",horastotales*dinero,"en total")
print("La empresa pago en total de", tra*horastot*dinero)