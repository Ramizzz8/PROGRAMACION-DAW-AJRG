import mysql.connector
conexion = mysql.connector.connect(
  host="local.host",
  user ="empresadam",
  password="Empresadam123$",
  database = "empresadam"
)
cursor= conexion.cursor()
cursor.execute('''
 SELECT * FROM clientes;
 ''')

filas = cursor.fetchall()

for filas in filas:
  print(fila)

cursor.close()
conexion.close()