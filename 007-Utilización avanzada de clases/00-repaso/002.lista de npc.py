class NPC():
  def __init__(self, x, y):
    self.x = x
    self.y = y

personajes = []

personajes.append(NPC(10, 20))
personajes.append(NPC(30, 40))

print(personajes)
