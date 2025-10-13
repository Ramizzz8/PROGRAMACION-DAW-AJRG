class Matematicas():
    def __init__(self):
        self.PI = 3.1416

    def redondeo(self,numero):
        entero = int(numero)
        decimal = numero - entero
        if decimal <0.5:
            redondea = 0
        else:
            redondea = 1
        return entero + redondea


    def techo(self,numero):
        return int(numero)+1  #Es +1 porque redondea a la alta, al hacerlo entero se queda en 4, al sumar mas 1 lo sube
    def suelo(self,numero):
        return int(numero)

Mate =  Matematicas()
print(Mate.redondeo(4.7))
print(Mate.redondeo(4.2))
print(Mate.techo(4.7))
print(Mate.suelo(4.7))