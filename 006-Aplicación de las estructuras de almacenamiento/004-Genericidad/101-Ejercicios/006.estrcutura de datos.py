<<<<<<< HEAD
numeros = [1,2,3,4,"cinco"]

print(numeros)

def calculaDoble():
    for numero in numeros:
        try:
            numero = int(numero)
            print(numero*2)
        except:
            print("No valido")
calculaDoble()
=======
numeros = [1,2,"3",4,"cinco"]

print(numeros)
numeros_etiquetas = ["cero","uno","dos","tres","cuatro","cinco"]
def calculaDoble():
  for numero in numeros:
    try:                    # Primero intenta convertir
      numero = int(numero)
      print(numero * 2)
    except:                 # Si no puedes
      # Intenta busca el valor en la lista de numeros
      for i in range(0,len(numeros_etiquetas)):
        if numero == numeros_etiquetas[i]:
          print(i*2)

calculaDoble()
>>>>>>> f886ffe8011f26e59a2456d7f0736f6627cb714a
