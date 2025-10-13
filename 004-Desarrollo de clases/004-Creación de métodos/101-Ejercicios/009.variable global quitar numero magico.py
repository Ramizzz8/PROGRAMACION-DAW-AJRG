limitediferenciasaldo = 1000 #Esta es una variable global que hace aclara de donde sale el 1000 que se encvontraba en la linea 12 (limite de saldo)

class CuentaBancaria():
    def __init__(self):
        self.__saldo = 0
        self.__cliente = ""

#Defino setter y getters para el saldo

def setSaldo(self, nuevosaldo):
    #Establezco una condicion de que valida si el saldo nuevo es mayor de 1000 euros
    if nuevosaldo >self.__ + limitediferenciasaldo:
        #Si salta la alarma, avisa y NO cambia el saldo
        print("Voy a avisar a la entidad de ingreso muy grande")
    else:
        #Si no es mayor de 1000
        self.__saldo

    self.__saldo = nuevo saldo

def getSaldo(self):
    return self.__saldo

cuentacliente1 = CuentaBancaria()
cuentacliente1.setsaldo(1000000)
print(cuentacliente1.getSaldo())