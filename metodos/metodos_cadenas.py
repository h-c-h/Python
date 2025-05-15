#"dir" -> no es un metodo, es una funcion.
#Permite ver todo los atributos de un objeto
#ojo tambien funciona con numero 1 , 2 , 3
#tambien con listas [] entre otros
cadena1 = "Buenos Dias"
cadena2 = "bienvenido a mi repositorio"
cadena3 = "12345"
cadena4 = "holacomoestas"
cadena5 = "como estas"
resultado = dir(cadena1) #->funcion
print(resultado)
#para usar un metodo tiene que ser("DATO.METODO()")

#"upper"
#convierte todo a mayuscula
mayuscula = cadena1.upper()
print(mayuscula)

#lower
#convierte todo a minuscula
minuscula = cadena1.lower()
print(minuscula)

#capitalize
#convierte la primer letra en mayuscula
primer_letra_mayuscula = cadena2.capitalize()
print(primer_letra_mayuscula)

#find
#lo que hace es buscar el valor que le pidamos 
# y nos dicen en que posicion esta
#ejemplo buscamos una cadena en otra cadena
#si no hay coincidencias devuelve "-1"
busqueda_find = cadena1.find("o")
print(busqueda_find)

#index
#lo que hace es buscar el valor que le pedimos
#osea exactamente lo mismo que en find
#pero la diferencia es que si en index no encuntra nada 
#nos devuelve un error mientras que en find nos devuelve "-1"
busqueda_index = cadena1.index("e")
print(busqueda_index)

#isnumeric
#si es numerico nos devolvera ture, sino devuelve false
es_isnumeric = cadena3.isnumeric()
print(es_isnumeric)

#isalpha
#si es alfanumerico nos devolvera true caso contrario devuelve false
#que quiere decir alfanumerico que solo acepta caracteres desde 
#la "A" hasta la "Z"
es_isalpha =  cadena4.isalpha()
print(es_isalpha)

#count
#lo que hace es buscar el valor que le pidamos pero
#nos devuelve la cantidad de veces que aparece en la cadena
contar_coindidencias = cadena2.count("i")
print(contar_coindidencias)

#len no es un metodo es una funcion
#lo que hace esta funcion es contar la cantidad de caracteres que
#tiene una cadena
#ESTO ESTA MAL->contar_caracteres = cadena1.len("")
contar_caracteres = len(cadena1)
print(contar_caracteres)

#startswith
#lo que hace es verificar si una cadena empieza con otra cadena dada
#si es asi devuelve True
empiza_con = cadena1.startswith("Bue")
print(empiza_con)

#endswith
#lo que hace es verificar si una cadena terminar con otra cadena dada
#si es asi devuelve True
termina_con = cadena1.endswith("as")
print(termina_con)

#replace
#lo que hace es reemplazar un pedazo de la cadena dada por otra dada.
#tambien si el valor 1, se encuntra en la cadena original
#reemplaza el valor 1 de la misma, por el valor 2
#                               valor1   valor2   
cadena_nueva = cadena5.replace("estas","bien")
print(cadena_nueva)

#split
#lo que va hacer es seprara cadenas con la cadena que le pasemos
cadena_separada = cadena2.split(" ")
print(cadena_separada)
print(cadena_separada[2])