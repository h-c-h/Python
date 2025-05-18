#Que es un dato compuesto: Son datos que adentro tiene datos simples
#o datos compuestos, que podemos agrupar

#Este tipo de datos es lista
lista=["Juan Zavala","Buenos Dias",True,1.75]
print(lista)
#Ahora imaginemos que quiero ingresar a uno de estos datos 
lista=["Juan Zavala","Buenos Dias",True,1.75]
print(lista[1])#->Porque no me dio como elemento 1 Juan Zavala
#Esto se debe a que en la programacion se cuenta del 0 al 9
#Imaginemos nuestro array "lista=["Juan Zavala","Buenos Dias",True,1.75]"
#Si le pedimos que nos pase el "dato 0" nos esta pasando el primer elemento
#que vendria hacer "Juan Zavala", esto se debe porque contamos desde el 
#cero hasta el ultimo elemento y la formacion seria de esta manera:

#Elemento1->"Juan Zavala"->lista[0]
#Elemento2->"Buenos Dias"->lista[1]
#Elemento3->True->lista[2]
#Elemento4->1.75->lista[3]

#Elemento1->"Juan Zavala"->lista[0]
#Porque "Juan Zavala" no puede ser el elemento 0 .¿Por qué? porque el
#elemento 0 no existe, entonces vendria hacer el elemento 1 
#que está alojado en el indice 0. Entonces, cuando nos referimos a
#índice es que posición esta. porque esto tiene posiciones.
#El indice 0 es la posción 0, el índice 1 es la posición 1 y asi
#sucesivamente.Entonces la posición es el índice y después esta el 
#de elementos.

#Entonces supongamos que queremos llamar a "Juan Zavala"
lista=["Juan Zavala","Buenos Dias",True,1.75]
print(lista[0])

#Ahora quiero llamar a 1.75
lista=["Juan Zavala","Buenos Dias",True,1.75]
print(lista[3])

#Otro tipo de datos compuestos son las tuplas
tupla=("Juan Zavala","Buenos Dias",True,1.75)
print (tupla[0])
#la tupla y la lista son casi lo mismo, cual es la diferencia
#la diferencia es que en la tupla nunca se va a poder modificar mientras
#que en la lista si puede modificarse

#Modificacion en solo lista
lista=["Juan Zavala","Buenos Dias",True,1.75]
lista[3]="Como estas"
print(lista[3])


#Esto no se puede hacer
#tupla=("Juan Zavala","Buenos Dias",True,1.75)
#tupla[3]="Como estas" 
# print(tupla[3])


#Creando un conjunto (set)
conjunto ={"Juan Zavala","Buenos Dias",True,1.75}
#para crear un conjunto set usamos llaves "{}" 
#la diferencia de un conjunto es que no tiene un orden fijo
#son elementos desordenados que pueden cambiar 
#digas "Juan Zavala" puede estar donde esta "Buenos Dias".
#En conjunto se puede modificar solo que los elementos no,
#es decir que se comporta como una tupla no podemos modificar elementos
#pero si podemos reconstruir.

# conjunto [1]="Pedro" -> no podemos modificar el elemento

#pero lo que si podemos hacer es
conjunto = {"Hola como esta tu día"}

#recontruccion de tupla
tupla = ("hola como esta tu día")

#La diferencia de conjunto que tiene con las listas es que no podemos
#acceder por el índice a un elemento del conjunto
#pero si podemos motrar como tal
conjunto ={"Juan Zavala","Buenos Dias",True,1.75}
print (conjunto)

#print(conjunto[1]) -> no puede acceder al elemento

#Unas de las caracteristicas del conjunto es no permite repetir valores
conjunto ={"Juan Zavala","Buenos Dias",True,1.75,"Juan Zavala"}
print (conjunto)
#Ahora imaginemos que lo agregamos a una lista y a una tupla
lista=["Juan Zavala","Buenos Dias",True,1.75,"Juan Zavala"]
print (lista)
tupla=("Juan Zavala","Buenos Dias",True,1.75,"Juan Zavala")
print (tupla)
#En la lista y tupla si se muestran y ¿Por qué? no en un cojunto
#porque en un cojunto no puede haber datos duplicados

#Creando un diccionario(dict)
diccionario = {
    'nombre':"Juan Zavala", 
    'saludo':"Buenos Dias",
    'esta_feliz':True,
    'altura':1.75,
    'dato_duplicado':"Juan Zavala"
}

#En una lista lo que muestra es esto:
#{
 #   0:"Juan Zavala", 
 #   1:"Buenos Dias",
 #   2:True,
 #   3:1.75,
 #   4:"Juan Zavala"
#}
#porque cuando a una lista le decimos mostrame el cuarto elemento
#en el tercer indice

#Por otra lado en diccionario lo muestra por nombre de asociado
diccionario = {
    'nombre':"Juan Zavala", 
    'saludo':"Buenos Dias",
    'esta_feliz':True,
    'altura':1.75,
    'dato_duplicado':"Juan Zavala"
}
print(diccionario['saludo'])
#El término en programación para esto es clave, valor estructura->(key:value)
#diccionario = {
#     key:value, 
#    'key':"value",
#    'key':value,
#    'key':1.value,
#    'key':"value"
#}