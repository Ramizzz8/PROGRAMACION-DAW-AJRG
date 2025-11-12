#Programa clase clientes
#v0.1 Andres Julian Ramirez Guerrrero
# Este programa crea una clase Clientes, se le añaden propiedades como Nombre, apellido, email y telefono(usando un metodo set y get para al menos una propiedad). Una vez creada la clase se crean tres instancias de la clase Clientes cada una con sus propiedades.
class Clientes():
    def __init__(self, nombre, apellido, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.__telefono = telefono  # Propiedad privada

    # Método getter para la propiedad telefono
    def get_telefono(self):
        return self.__telefono

    # Método setter para la propiedad telefono
    def set_telefono(self, telefono):
        self.__telefono = telefono
# Crear instancias de la clase Clientes
cliente1 = Clientes("Juan", "Pérez", "juan.perez@example.com", "123456789")
cliente2 = Clientes("Ana", "Gómez", "ana.gomez@example.com", "987654321")
cliente3 = Clientes("Luis", "Martínez", "luis.martinez@example.com", "456789123")
# Demostrar que lso metodos set y get funcionan correctamente

# Demostrar funcionamiento de los métodos get y set
print("Teléfonos originales:")
print(cliente1.get_telefono())
print(cliente2.get_telefono())
print(cliente3.get_telefono())

# Modificar los teléfonos
cliente1.set_telefono("111222333")
cliente2.set_telefono("444555666")
cliente3.set_telefono("777888999")

print("Teléfonos modificados:")
print(cliente1.get_telefono())
print(cliente2.get_telefono())
print(cliente3.get_telefono())







