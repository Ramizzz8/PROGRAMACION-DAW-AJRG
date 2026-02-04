<!doctype html>
<html lang="es">
  <head>
    <title>Tienda</title>
    <style>
/* ======================================================
   LOONEY TUNES – DESKTOP (PC)
   ====================================================== */

@import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@700&display=swap');

body {
  font-family: 'Comic Neue', cursive;
  background: radial-gradient(circle at top, #fff3a0, #ffb347);
  color: #000;
}

/* Header */
header {
  background: linear-gradient(135deg, #ff3131, #ff914d);
  border-bottom: 6px solid #000;
}

header h1 {
  text-shadow: 4px 4px 0 #000;
  letter-spacing: 3px;
}

/* Main layout */
main {
  display: grid;
  grid-template-columns: 1fr;
  gap: 3rem;
}

/* Sections */
section {
  border: 5px solid #000;
  box-shadow: 8px 8px 0 #000;
  background: #fff;
  max-width: 1100px;
  margin: 0 auto;
}

/* Productos grid */
#productos div {
  display: grid;
  grid-template-columns: repeat(3, minmax(220px, 1fr));
  gap: 2.5rem;
  justify-items: center;
}

/* Product card */
article {
  background: #baffc9;
  border: 4px solid #000;
  box-shadow: 6px 6px 0 #000;
  padding: 2rem;
  width: 100%;
  max-width: 260px;
  transform: rotate(-1deg);
}

article:nth-child(2) {
  background: #bae1ff;
  transform: rotate(1deg);
}

article:nth-child(3) {
  background: #ffb7ce;
  transform: rotate(-2deg);
}

article:hover {
  transform: scale(1.08) rotate(0deg);
}

article h4 {
  font-size: 1.3rem;
  margin-bottom: 1.2rem;
}

/* Buttons */
button {
  width: 100%;
  background: #ffe600;
  border: 4px solid #000;
  box-shadow: 4px 4px 0 #000;
  font-size: 1.1rem;
}

button:hover {
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0 #000;
}

/* Cliente form */
section:last-of-type > div {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  max-width: 700px;
  margin: 0 auto;
}

#enviar {
  grid-column: span 2;
  text-align: center;
  background: #00e5ff;
  border: 4px solid #000;
  box-shadow: 5px 5px 0 #000;
}

/* ======================================================
   LOONEY TUNES – MOBILE (≤ 768px)
   ====================================================== */

@media (max-width: 768px) {

  header h1 {
    font-size: 1.7rem;
  }

  main {
    gap: 2rem;
  }

  section {
    margin: 0 0.5rem;
    padding: 1.5rem;
  }

  #productos div {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  article {
    max-width: 100%;
    transform: rotate(0deg);
  }

  section:last-of-type > div {
    grid-template-columns: 1fr;
  }

  #enviar {
    grid-column: auto;
  }
}
    </style>
    <meta charset="utf-8">
  </head>
  <body>
    <header>
      <h1>Microtienda</h1>
    </header>
    <main>
      <section id="productos">
        <h3>Productos</h3>
        <div>
          <?php
            $host = "localhost";
            $user = "microtienda";
            $pass = "Microtienda123$";
            $db   = "microtienda";
            $conexion = new mysqli($host, $user, $pass, $db);
            $sql = "SELECT * FROM productos;";
            $resultado = $conexion->query($sql);
            while ($fila = $resultado->fetch_assoc()) {
          ?>
            <article>
              <h4><?= $fila['nombre'] ?></h4>
              <button nombre="<?= $fila['nombre'] ?>"><?= $fila['precio'] ?>€</button>
            </article>
          <?php }?>
        </div>
      </section>
      <section>
        <h3>Datos de cliente</h3>
        <div>
          <input type="text" id="nombre" placeholder="Nombre">
          <input type="text" id="apellidos" placeholder="Apellidos">
          <input type="text" id="email" placeholder="Email">
          <div id="enviar">Enviar pedido</div>
        </div>
      </section>
    </main>
    <footer>
      (c) 2026 Andres Ramirez
    </footer>
  </body>
  <script>
    var fecha = new Date();
    var pedido = {
    	cliente:{},
      productos:[],
      pedido:{
      	"numero":Date.now(),
        "fecha":fecha.getFullYear()+"-"+(fecha.getMonth()+1)+"-"+fecha.getDate()
      }
    };
    /////// Atrapa productos y los mete en el carro
    let botones = document.querySelectorAll("button");
    botones.forEach(function(boton){
    	boton.onclick = function(){
      	pedido.productos.push({
          "nombre":this.getAttribute("nombre"),
        	"precio":this.textContent
        })
        console.log(pedido)
      }
    })
    console.log(pedido)
    /////// Atrapa los datos del cliente
    let boton_enviar = document.querySelector("#enviar");
    boton_enviar.onclick = function(){
      let nombre_cliente = document.querySelector("#nombre").value;
      let apellidos_cliente = document.querySelector("#apellidos").value;
      let email_cliente = document.querySelector("#email").value;
      pedido.cliente = {
        "nombre":nombre_cliente,
        "apellidos":apellidos_cliente,
        "email":email_cliente
      }
      console.log(pedido)
    }
    //Y los envio para guardar
    fetch("guardamongo.php"?+JSON.stringify(pedido))
  </script>
</html>