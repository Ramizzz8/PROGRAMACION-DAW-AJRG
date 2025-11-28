class npc():
  def __init__(self, x, y):
    self.x = x
    self.y = y

personajes = []
numero_personajes = int(50)

for i in range(0, numero_personajes):
  personajes.append(npc(4,3))

print(personajes)
