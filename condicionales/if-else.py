#Una condicional son basicamente padacitos de codigo que nos dicen
#si condicion se cumple -> si es true se va a ejecutar si es falso no ejecuta
  #codigo que ejecutara en caso
  #que la condicion se cumpla
  
#Ademas tenemos la posibilidad de decirle, si esta condicion no se cumple
#osea si lo de arriba es false no vamos a ejecutar el codigo de arriba,
#vamos a ejecutar el codigo de abajo

#si condicion se cumple: -> no se ejecutario porque no se cumple
 #codigo a ejecutar en caso
 #que la condicion se cumpla
#de lo contrario:-> este si se ejecutaria
 #codigo a ejecutar en caso de
 #que la condicion No se cumpla
edad = 15
if edad >=18 :
    print("Eres mayor")
else:
    print("No eres mayor")
 
contraseña_almacenada = "hola"
contraseña_escrita = "hola"
if contraseña_almacenada == contraseña_escrita:
    print("Inciando Sesion...")
else:
    print("Contraseña equivocada, intente de nuevo")