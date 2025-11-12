class Cliente():
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        
print("##########PROGRMA GESTION DE CLIENTES v0.1#############")
print("----------###########BIENVENIDO############------------")

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
        clientes.append(Cliente(nombre, apellidos, email))
    elif opcion == 2:
        identificador = 0
        for cliente in clientes:
            print("Este es el cliente con ID: ", identificador)
            print(cliente.nombre, cliente.apellidos, cliente.email)
            identificador += 1    #esto le suma 1 a cada vez que se introduce un cliente nuevo
            
    elif opcion == 3:
        identificador = int(input("Introduce el identificador para modificar: "))
        nombre = input("Cual es el nombre del cliente: ")
        apellidos = input("Cuales son los apellidos del cliente: ")
        email = input("Cual es el email del cliente: ")
        clientes[identificador].nombre = nombre
        clientes[identificador].apellidos = apellidos
        clientes[identificador].email = email
    elif opcion == 4:
        identificador = int(input("Introduce el identificador para eliminar: "))
        confirmacion = print("Estas seguro? (S/N): ")
        if confirmacion == 'S' or confirmacion == 's':
            clientes.pop(identificador)
        elif confirmacion == 'N' or confirmacion == 'n':
            print ("Cancelado")
        else:
            print("No valido!")

