<!doctype html>
<html>
	<head>
        <style>
        form {
            display: flex;
            flex-direction: column;
            width: 300px;
            margin: auto;
            }
        label, input {
            margin-bottom: 10px;
            }
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
            justify-content: center;
            align-items: center;
            display: flex;
            height: 100vh;
            flex-direction: column;

            }
            h1 {
            text-align: center;
            margin-bottom: 30px;
            }
        header, main, footer {
            margin-bottom: 20px;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
        </style>
  	<style>
    	
    </style>
  </head>
  <body>
  	<header>
  		<h1>Preguntas y respuestas</h1>
    </header>
    <main>
    	<form action="?" method="POST">
      	<label for="pregunta">Introduce la pregunta</label>
      	<input type="text" name="pregunta" id="pregunta">
        <label for="respuesta">Introduce la respuesta</label>
      	<input type="text" name="respuesta" id="respuesta">
        <input type="submit">
      </form>
    </main>
    <footer>
      <?php
      	if(isset($_POST['pregunta']) && isset($_POST['respuesta'])){
          echo $_POST['pregunta'];
          echo "<br>";
          echo $_POST['respuesta'];
        }
      ?>
    </footer>
  </body>
</html>