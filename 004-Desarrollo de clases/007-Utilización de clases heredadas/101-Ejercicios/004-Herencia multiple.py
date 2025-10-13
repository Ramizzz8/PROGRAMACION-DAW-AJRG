class Entidad():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

class Animal():
    def __init__(self):
        self.edad = 0
        self.nombre = ""
        self.raza = ""
        
class Gato(Animal):
    def __init__(self):
        super().__init__()

class Perro(Animal):
    def __init__(self):
        super().__init__()   #Me traigo todo lo que tenga la clase superior o de la que se herda la propiedad

class Roca(Entidad):
    def __init__(self):
        super().__init__()


gato1 = Animal()
print(gato1.edad)

perro1 = Animal()
print(gato2.edad)