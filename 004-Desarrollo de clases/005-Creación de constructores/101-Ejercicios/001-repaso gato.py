class Gato():
    def __init__(self): #El constructor se ejecuta si o si
        self.edad = 0
    
    def maulla (self):
        return "El gato esta maullando"


gato1 = Gato()
print(gato1.edad)

print(gato1.maulla())
