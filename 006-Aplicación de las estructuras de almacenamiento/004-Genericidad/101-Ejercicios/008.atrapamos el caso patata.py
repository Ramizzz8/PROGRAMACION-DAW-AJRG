numeros = [1,2,"3",4,"cinco","patata"]

print(numeros)
numeros_etiquetas = ["cero","uno","dos","tres","cuatro","cinco"]
def calculaDoble():
  for numero in numeros:
    try:                    # Primero intenta convertir
      numero = int(numero)
      print(numero * 2)
    except:
      centinela = False                 # Si no puedes
        # Intenta busca el valor en la lista de numeros
        for i in range(0,len(numeros_etiquetas)):
          if numero == numeros_etiquetas[i]:
            print(i*2)
            centinela = True
          if centinela = False:
            print("Lo intente pero no se pudo")

calculaDoble()

#Explica que hace el codigo
# El código define una lista llamada "numeros" que contiene una mezcla de enteros y cadenas de texto que representan números y una palabra no numérica ("patata"). Luego, imprime esta lista.
# A continuación, define otra lista llamada "numeros_etiquetas" que contiene las representaciones en texto de los números del 0 al 5.
# La función "calculaDoble" recorre cada elemento de la lista "numeros". Para cada elemento, intenta convertirlo a un entero y, si tiene éxito, imprime el doble de ese número.
# Si la conversión falla (lo que ocurre con las cadenas de texto), entra en el bloque "except". Aquí, busca el elemento en la lista "numeros_etiquetas". Si encuentra una coincidencia, imprime el doble del índice correspondiente.
# Si no encuentra ninguna coincidencia (como en el caso de "patata"), imprime un mensaje indicando que no se pudo realizar la operación.

