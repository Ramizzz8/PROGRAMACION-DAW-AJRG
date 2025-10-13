class Cliente():
    def __init__(self):
        self.nombrecompleto = ""
        self.email = ""
    def setNombreCompleto(self,nuevonombre):
        self.nombrecompleto = nuevonombre
    def setEmail(self,nuevoemail):
        self.email = nuevoemail
    def getNombreCompleto(self):
        return self.nombrecompleto
    def getEmail(self):
        return self.email

# CRUD - Creat, Read, Update, Delete

#Creo lista

clientes = []

while True:
    print("Gestor de clientes v0.1 Andres Ramirez")
    print("Selecciona una opcion")
    print("1-Insertar un nuevo cliente")
    print("2-Obtener un listado de clientes")
    opcion = int(input("Indica tu opcion(1,2)"))

    #Compruebo si la opcion es valida con IF

    if opcion == 1:
        print("Voy a insertar un cliente")
        nuevocliente = Cliente()
        nombrecliente = input("Introduce el nombre del cliente: ") #tomo el dato
        nuevocliente.setNombreCompleto(nombrecliente) #Uso el metodo set para meter el dato en el objeto
        emailcliente = input("Introduzca el email del cliente: ")
        nuevocliente.setEmail(emailcliente)
        clientes.append(nuevocliente)
    elif opcion == 2:       #Los getters se usan en operaciones de listado
        print("Saco el listado de clientes")
        for cliente in clientes:
            print("--------------------------------")
            print("Nombre: ",cliente.getNombreCompleto())
            print("Email: ",cliente.getEmail())
            print("--------------------------------")
    else:
        print("Opcion no valida")


