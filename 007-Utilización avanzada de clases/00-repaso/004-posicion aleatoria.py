import random

class npc():
  def __init__(self, x, y):
    self.x = x
    self.y = y

personajes = []
numero_personajes = int(50)

for i in range(0, numero_personajes):
  x_alt=random.randint(0,500)
  y_alt=random.randint(0,500)
  personajes.append(npc(x_alt,y_alt))

print(personajes)
