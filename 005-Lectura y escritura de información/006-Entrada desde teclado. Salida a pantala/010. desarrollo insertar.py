class Cliente():
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        
print("##########PROGRMA GESTION DE CLIENTES v0.1#############")
print("###########BIENVENIDO############")

clientes = []

while True:
    print("Escoge una opcion: ")
    print("1.-Insertar un cliente ")
    print("2.-Listar clientes ")
    print("3.-Actualizar clientes")
    print("4.-Eliminar clientes")
    opcion = int(input("Escoge una opcion: "))

    if opcion == 1:
        nombre = input("Cual es el nombre del cliente: ")
        apellidos = input("Cuales son los apellidos del cliente: ")
        email = input("Cual es el email del cliente: ")
    if opcion == 2:
    
    if opcion == 3:
    
    if opcion == 4:


