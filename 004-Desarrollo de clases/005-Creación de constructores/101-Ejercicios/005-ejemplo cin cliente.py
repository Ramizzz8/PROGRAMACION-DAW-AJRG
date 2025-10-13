class Cliente():
    def __init__(self,nombre, apellidos, email, direccion): #El constructor se ejecuta si o si
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion

clientes = []
while True:

    nombre = input("Introduce el nombre del cliente: ")
    apellidos = input("Introduce los apellidos de cliente: ")
    email = input("Introduce el email del cliente: ")
    direccion = input("Introduce la direccion del cliente: ")

    clientes.append(Cliente(nombre,apellidos,email,direccion))


