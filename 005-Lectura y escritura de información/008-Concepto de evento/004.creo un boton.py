import tkinter as tk

ventana = tk.Tk()

def insertar():
    print("Hola")

marco= tk.Frame(ventana)

#DNI / NIE
tk.Label(marco,text="Introduce el DNI/NIE del cliente: ").pack(padx=10,pady=10)
dninie= tk.Entry(marco)
dninie.pack(padx=10,pady=10)
#Nombre
tk.Label(marco,text="Introduce el nombre del cliente: ").pack(padx=10,pady=10)
nombre= tk.Entry(marco)
nombre.pack(padx=10,pady=10)
#Apellidos
tk.Label(marco,text="Introduce los apellidos del cliente: ").pack(padx=10,pady=10)
apellidos= tk.Entry(marco)
apellidos.pack(padx=10,pady=10)
#Email
tk.Label(marco,text="Introduce el email del cliente: ").pack(padx=10,pady=10)
email= tk.Entry(marco)
email.pack(padx=10,pady=10)

#Boton
tk.Button(marco,text="Insertar cliente",command = insertar ).pack(padx=10, pady=10)

marco.pack(padx=10,pady=10)

ventana.mainloop()