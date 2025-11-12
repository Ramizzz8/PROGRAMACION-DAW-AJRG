from flask import Flask
aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    return '''
    <!DOCTYPE html>
<html lang="en">
    <head>
        <title>RAMI-BLOG</title>
        <meta charset="UTF-8">
        <style>
            body{background: wheat;color: black;font-family: 'Times New Roman', Times, serif;}
            header,main,footer{background: whitesmoke;padding: 20px; margin: auto ;width: 600px;}
            header,footer{text-align: center;}
            main{color: black;}
        </style>
    </head>
    <body>
        <header><h1>RAMI-BLOG</h1></header>
        <main>
            <article>
                <h3>Titulo del articulo</h3>
                <time datetime="">16-10-2025</time>
                <p>Andres Julian Ramirez Guerrero</p>
                <p>Este es el contenido de un articulo ficticio</p>
            </article>
        </main>
        <footer>(c) Andres Ramirez - Alias Little Dimon</footer>   
    </body>
</html>
'''

if __name__ == "__main__":
    aplicacion.run(debug=True)