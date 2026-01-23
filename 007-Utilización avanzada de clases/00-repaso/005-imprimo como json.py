import random
import json

class npc():
    def __init__(self, x, y):
        self.posx = x
        self.posy = y

    # Método para convertir el objeto en diccionario
    def to_dict(self):
        return {"posx": self.posx, "posy": self.posy}

personajes = []
numero_personajes = 50

for i in range(0, numero_personajes):
    xalt = random.randint(0, 500)
    yalt = random.randint(0, 500)
    personajes.append(npc(xalt, yalt))

# Convertimos todos los npc a diccionarios
personajes_json = [p.to_dict() for p in personajes]

# Lo imprimimos formateado
print(json.dumps(personajes_json, indent=2))
