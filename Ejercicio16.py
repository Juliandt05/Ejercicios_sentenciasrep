horastot = 0
tra = int(input("Cuantos trabajadores tiene la empresa"))
dinero = int(input("Cuanto cobra cada hora"))
for x in range(1,7):
    print("Cuántas horas ha trabajado hoy")
    horas = int(input())
    horastotales = horas + horastotales
print("El sueldo de los", tra,"son de",horastotales*dinero,"en total")
print("La empresa pago en total de", tra*horastot*dinero)