#keys
#lo que hace keys es que nos devuelve la clave
#tambien se puede iterar 
diccionario={
#   clave :   valor
    "nombre":'anthony',
    "apellido":'zava',
    "edad":18
}

claves = diccionario.keys()
print(claves)

#get
#con get() obtenemos un elemento (si no encuentra dicho elemento el programa
# continua y no tira excepciones)
valor_get = diccionario.get("nombre")
prueba_error = diccionario.get("no esta")
print(prueba_error)
print(valor_get)

#pop
#elimina un elemento del diccionario
diccionario.pop("nombre")
print(diccionario)

#items
#aca obetenemos un elemento dict_items iterable
dicc_items = diccionario.items()
print(dicc_items)