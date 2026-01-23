agenda =[]

while True:
  nombre = input("Dime tu nombre: ")
  apellido = input("Dime tu apellido: ")
  email = input("Dime tu email: ")
  telefono = input("Dime tu telefono: ")
  #añado a la agenda
  agenda.append([nombre, apellido, email, telefono])
  print(agenda)
