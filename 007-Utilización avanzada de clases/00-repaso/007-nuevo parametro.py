import random
import json
from flask import Flask, render_template

class npc():
    def __init__(self, x, y, radio):
        self.posx = x
        self.posy = y
        self.radio = radio

    # Método para convertir el objeto en diccionario
    def to_dict(self):
        return {"posx": self.posx, "posy": self.posy, "radio":self.radio}

personajes = []
numero_personajes = 50

for i in range(0, numero_personajes):
    xalt = random.randint(0, 500)
    yalt = random.randint(0, 500)
    radioalt = random.randint(10, 30)
    personajes.append(npc(xalt, yalt, radioalt))

# Convertimos todos los npc a diccionarios
personajes_json = [p.to_dict() for p in personajes]

# Lo imprimimos formateado
print(json.dumps(personajes_json, indent=2))

#flask
app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template("juego.html")

@app.route("/api")
def api():
  return json.dumps(personajes_json, indent=2)

if __name__ == "__main__":
  app.run(debug=True)
