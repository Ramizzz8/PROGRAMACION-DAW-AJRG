class Gato():
    def __init__:
    self.color = "" #Esto es una propiedad

    def maulla (self):  #Esto es un metodo (es una accion)
        return "miau"
    
    def setColor(self, nuevocolor): #defino un setter- el metodo es el responsable de cambiar la propiedad
        #Por ejemplo aqui podria validar si el color es un color valido para un gato
        self.color = nuevocolor #Cambio la propiedad
    
    def getColor(self):
        return self.color
