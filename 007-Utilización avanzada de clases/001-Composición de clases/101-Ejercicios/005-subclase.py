class Persona():
  def __init__(self,nombre,apellidos,email,direccion):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    self.direccion = direccion
  def dameDatos(self):
    return self.nombre+self.apellidos

class Profesor(Persona):
  def __init__(self,nombre,apellidos,email,direccion):
  	super().__init__(nombre, apellidos, email,direccion)

class Alumno(Persona):
  def __init__(self,nombre,apellidos,email,direccion):
    super().__init__(nombre, apellidos, email,direccion)
class AlumnoOnline(Alumno):
  def __init__(self,nombre,apellidos,email,direccion,plataforma):
    super().__init__(nombre, apellidos, email,direccion)
    self.plataforma = plataforma
class AlumnoPresencial(Alumno):
  def __init__(self,nombre,apellidos,email,direccion,aula):
    super().__init__(nombre, apellidos, email,direccion)
    self.aula = aula

alumno1 = Alumno("Andres Julian ","Ramirez","info@andres.com","Direccion falsa 123")
print(alumno1.dameDatos())

profesor1 = Profesor("Juan ","Garcia","juan@jocarsa.com","Direccion verdadera 456")
print(profesor1.dameDatos())
