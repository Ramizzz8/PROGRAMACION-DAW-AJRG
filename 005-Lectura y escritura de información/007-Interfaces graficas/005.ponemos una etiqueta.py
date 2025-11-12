import tkinter as tk

ventana = tk.Tk()

def accion():
    print("CALLING NIGGA-MAN")

tk.Button(ventana,text="Click me", command = accion).pack(padx=10, pady=10)

etiqueta = tk.Label(text="¿Has pulsado el boton?")
etiqueta.pack(padx= 10, pady=10)

ventana.mainloop() #Es decirle que no se salga
