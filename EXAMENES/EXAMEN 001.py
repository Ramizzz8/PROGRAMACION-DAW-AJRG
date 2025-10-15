'''
PROGRAMA DE REGISTRAR PRODUCTOS
v0.1 ANDRES JULIAN RAMIREZ GUERRERO
Este programa gestiona productos
'''

#Defino variables
nombre_producto = input("Cual es el nombre del producto: ")#Uso input para que el usuario introduzca informacion
cantidad_producto = int(input("Cual es la cantidad en stock: "))#Uso int para dejar claro que tiene que ser un valor numerico 
precio_base = int(input("Cual es el precio del producto: "))
iva = 1.21
precio_iva = (precio_base * iva)


#Creo condicional para comprobar stock
if  cantidad_producto > 0:
    print("El producto esta disponible")#Imprimo si el producto esta disponible solo SI la cantidad es mayor a 0
elif cantidad_producto < 5:
    print("El stock es bajo")#Si la cantidad es menor que 5 informo que hay bajo stock del producto


#Muestro los datos del producto ( ofrezco resultados)
print("Los datos del producto son:")
print(nombre_producto)
print("Su precio base es de", precio_base,"€")
print("Su precio con IVA es de", precio_iva, "€")
print("En stock hay", cantidad_producto)