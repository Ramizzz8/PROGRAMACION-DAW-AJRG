import tkinter as tk

ventana = tk.Tk()

tk.Button(ventana,text="Click me", command = accion).pack(padx=10, pady=10)

ventana.mainloop() #Es decirle que no se salga
