
from tkinter import *
from tkinter import ttk

def saludar():
    texto=campoTexto.get()
    print(texto)
    textoLabel.set(texto)


#Generar la ventana
ventana = Tk()
ventana.title("Primer ejercicio")
ventana.geometry("300x100")
ventana.resizable(width=False,height=False)
ventana.config(background="Light Blue")
#Generar el lienzo para pintar componentes
frm = ttk.Frame(ventana, padding=10).pack()
#Componentes Label y button
textoLabel=StringVar()
textoLabel.set("Hola Tkinter")
labelTexto = ttk.Label(frm, textvariable=textoLabel) 
labelTexto.config(background="blue",border=5,font=("Arial",15))
labelTexto.pack()
ttk.Button(frm, text="Salir", command=ventana.destroy).pack()

# Componente
campoTexto=ttk.Entry(frm)
campoTexto.pack()



ttk.Button(frm, text="Saludo",command=saludar).pack()
ttk.Button(frm, text="Salir",command=ventana.destroy).pack()


#
ventana.mainloop()