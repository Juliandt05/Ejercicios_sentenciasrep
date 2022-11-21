
from tkinter import *
from tkinter import ttk

def saludar():
    texto=campoTexto.get()
    print(texto)


#Generar la ventana
ventana = Tk()
ventana.title("Primer ejercicio")
ventana.geometry("300x100")
ventana.resizable(width=False,height=False)
ventana.config(background="Blue")
#Generar el lienzo para pintar componentes
frm = ttk.Frame(ventana, padding=10).pack()
#Componentes Label y button
labelTexto = ttk.Label(frm, text = "Hola Tkinter") 
labelTexto.config(background="red",border=5,font=("Arial",15))
labelTexto.pack()
ttk.Button(frm, text="Salir", command=ventana.destroy).pack()

# Componente
campoTexto=ttk.Entry(frm)
campoTexto.pack()



ttk.Button(frm, text="Saludo",command=saludar).pack()
ttk.Button(frm, text="Salir",command=ventana.destroy).pack()


#
ventana.mainloop()