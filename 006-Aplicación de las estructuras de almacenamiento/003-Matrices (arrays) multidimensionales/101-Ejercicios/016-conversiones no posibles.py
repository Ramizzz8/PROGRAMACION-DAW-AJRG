<<<<<<< HEAD
import pickle
agenda =[]

while True:
  nombre = input("Dime tu nombre: ")
  apellido = input("Dime tu apellido: ")
  email = input("Dime tu email: ")
  telefono = input("Dime tu telefono: ")
  #añado a la agenda
  agenda.append([nombre, apellido, email, telefono])
  print(agenda)
  archivo = open("agenda.pickle", "wb")
  pickle.dump(agenda, archivo)
  archivo.close()
=======
edad = "a"

edad_en_entero = int(edad)

print(edad)
print(edad_en_entero)
>>>>>>> f886ffe8011f26e59a2456d7f0736f6627cb714a
