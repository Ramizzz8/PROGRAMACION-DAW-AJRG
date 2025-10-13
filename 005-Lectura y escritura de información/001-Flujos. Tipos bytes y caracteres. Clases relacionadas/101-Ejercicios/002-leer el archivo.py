archivo = open("clientes.txt",'r') # R de READ 

contenido = archivo.readline()
#Tambien existe archivo.readlines()

print(contenido)

archivo.close()