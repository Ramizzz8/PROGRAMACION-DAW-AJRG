import pickle
agenda =[]

while True:
  #insertar
  nombre = input("Dime tu nombre: ")
  apellido = input("Dime tu apellido: ")
  email = input("Dime tu email: ")
  telefono = input("Dime tu telefono: ")
  #añado a la agenda
  agenda.append([nombre, apellido, email, telefono])
  #imprimir
  print(agenda)
  #guardar
  archivo = open("agenda.pickle", "wb")
  pickle.dump(agenda, archivo)
  archivo.close()
