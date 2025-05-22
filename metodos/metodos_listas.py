#list ->esta es una funcion
#creas una lista con list()
lista = list(["adios","david",35,53,12,True])
print(lista)

#len->funcion
#lo que hace es devolver la cantidad de elementos que hace una lista
cantidad_elementos = len(lista)
print(cantidad_elementos)

#append
#lo que hace es agregar elementos a una lista
#append solo acepta un argumento
lista.append("mmmmmm")
print(lista)

#insert
#lo que hace es agrega un elemento a la lista en un indice especifico
#         indice  elemento 
lista.insert(2,"como estas")
print(lista)

#extend
#con extend podemos agrgar varios elementos a la lista
#lista.extend(False,2030)-> para agregar un elemento a una lista le
#tenemos que pasar una lista. es decir, agregarmos una lista dentro de 
#otra lista
lista.extend([False,2003])
print(lista)

#pop
#esto elimina un elemento de una lista(por su indice). por qué 
#pones por su indice porque pop nos pide el indice
#para quere eliminar el ultimo elemento de una lista  
#podemos usar "lista.pop(-1)". esto es una tecnica en vez de contar
#cual es el ultimo indice . podemos poner el -1 para elimar el ultimo
#elemento tambien podemos usar (-2) para el penuntimo y asi sucesivamente
lista.pop(-1)
print(lista)

#remove
#elimina un elemento de una lista por su valor
lista.remove("david")
print(lista)

#sort
#ordena los elemento de forma acendente
#sort solo funcion si tiene numeros o booleanos, si tiene cadena de texto
#nos manda error
#los false son primero los true segunda y después viene los numeros
#del menor al mayor
listado = list([84,20,12,34,58,99,True,False])
listado.sort()
print(listado)
#si usamos el parametro reverse =true dentro de sort
#lo que hace es ordenar en reversa la lista
listado.sort(reverse=True)
print(listado)

#reverse
#lo que hace es invertir los elementos de una lista sin ordenarlos
#aca si podemos usar un str o cadena
listados = list(["hola",82,35,40,20,True])
listados.reverse()
print(listados)

#clear
#esto elimina todos los elementos de la lista
lista.clear()
print(lista)