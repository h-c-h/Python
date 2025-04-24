#Sirve para almacenar información
a=15
b= 8
c=a+b
print (c)

#Las variables son modificables
nombre = "juan" #-> aca definimos a nombre como juan
nombre = "vega" #-> aca ahora estamos redefiniendo a nombre como vega
nombre = "lucas" #->y podemos seguir redefiniendo sucesivamente
print (nombre)

#ahora con numeros
numero = 10
numero +=1 #-> El "+=" esto es una forma abreviada de codificar 
#"numero=numero +1" en vez de poner eso codificamos "numero +=1"
numero -=5
print(numero)


#CONCATENACION(unimos cadenas)
#concatenar con +
name = "Pedro"
bienvenida = "Hola "+ name + " ¿Como esta?" #-> Esta forma solo es para 
# tipo string ya que para tipo numerico no funcionaria
print (bienvenida)

#concatenar con f
#.format
Nombre = "Cristian"
bienvenido = f"Hola {Nombre} ¿Como esta?" #-> El ".format" lo que hace es
# tomar un dato y convertirlo a texto no importa si es numero o booleano
print (bienvenido)

#Ejemplo dato booleano
booleano = True
bienvenido = f"Hola {booleano} ¿Como esta?"
print (bienvenido)

#Ejemplo dato numero
Numero = 6
bienvenido = f"Hola {numero} ¿Como esta?"
print (bienvenido)

#Si queremos hacer que una variable no este mas declarada
#usamos el operador "del"
number = 8
adios = f"Adios {number}"
#del adios 
print(adios)#-> nos mostrar error ya que no tenemos una variable definida
# "adios" porque lo acabmos de borrar con "del"


#Ahora si queremos borrar "number", el codigo seguire compilando normal
#esto se debe a que el "number" lo borre después de declarar adios
number = 8
adios = f"Adios {number}"#->aca number ya esta definido
#del number #->aca estoy borrando number
print(adios)
#entonces para poder borrar el "number" tenemos que colocar antes
number = 8
#del number
adios = f"Adios {number}"
print(adios)
#Si queremos que el codigo funcione solo borramos "del"


#Operadores de Pertenecia y Operadores de Identidad

#Operadores de Pertenencia (in/not in)
nombre= True
bienvenida = f"Hola {nombre} ¿Como estas?"
print ("ola"in bienvenida)#-> Aca me va a decir que es True porque el
#pedacito de texto "ola" si esta en la variable bienvenida "H (o l a)"
nombre= True
bienvenida = f"Hola {nombre} ¿Como estas?"
print ("pedro"in bienvenida)#->Me va a decir False porque pedro no se
#encuentra en la variable bienvenida

nombre= True
bienvenida = f"Hola {nombre} ¿Como estas?"
print ("pedro" not in bienvenida)#->Si colocamos not in nos va a decir
#True porque es verdad pedro no esta en el bienvenida pero si ponemos Hola

nombre= True
bienvenida = f"Hola {nombre} ¿Como estas?"
print ("Hola"not in bienvenida)# ->Nos dice que es False porque 
#porque "Hola" no esta en bienvenida, pero Hola si esta en bienvenida 
#entonces seria falso
#Ojo si ponemos ("hola"in bienvenida) sin mayúscula el nos dara false
#ya que le programa es un leguaje case sensitive es sensible a 
#masyúsculas y minúsculas

#Definiendo una variable con camelCase
nombreEscribeTuNombreCompleto = "Jose Hurtado"
#Definiendo una variable con snake_case
nombre_escribe_tu_nombre_completo = "Jose Hurtado"