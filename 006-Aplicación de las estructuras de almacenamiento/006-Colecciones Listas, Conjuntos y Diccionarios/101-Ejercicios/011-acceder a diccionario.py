
persona = {
  "nombre":"Andres Julian",
  "apellidos":"Ramirez Guerrero",
  "correo":"info@andres.com",
  "edad":17,
  "telefonos":[
  	{	
      "tipo":"fijo",
    	"número":96123455
    },
    {	
      "tipo":"movil",
    	"número":65456546
    }
  ]
}

print(persona)
print(persona["telefonos"][0]["número"])