#Las propiedades son como variables PERO dentro de una clase

class Cliente():
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.telefonos = {'60083654','8764383'}

#Ahora instancio un nuveo objeto
cliente1 = Cliente()

#Ahorea le escribo una propiedad

cliente1.nombre = "Jose Vicente"

print ("El nombre del cliente es :", cliente1.nombre)

#Añado a la clase los telefonos

cliente1.telefonos.append("60083654")
cliente1.telefonos.append("8764383")

print(cliente1.telefonos)
 