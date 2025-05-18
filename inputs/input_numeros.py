#input
#pedir un numero al usuario
numero = input("dame un numero: ")

#multiplicalo por 3
resultado = numero * 3
#si le damos el numero 2 a 'numero'
print(resultado)#->no da 222 por qué.
#explicacion
#aca el 2 viene a hacer un texto, cuando agarramos el texto y lo sumamos o
#multiplicamos simplemente se suman los caracteres
#osea si a 'numero' le damos el valor de 4 que viene a ser texto y si a ese
#texto lo multiplico por 3 vendria hacer '444'
# "2"*3="222"

#ahora cuando al numero lo multiplicacomos por 2 tenemos el resultado
#de una operacion aritmetica, estamos trabajando aritmeticamente con el dato
#entonces para poder trabajar aritmeticamente debemos convertirlo a numero

#  2*3 = 6

#converti numero a entero y lo multiplicamos 3
numero1 = input("dame un numero: ")
respuesta_int = int(numero1) * 3
print(respuesta_int)
#converti numero a flotante y lo multiplicamos 3
numero2 = input("dame un numero: ")
respuesta_float = float(numero2) * 3
print(respuesta_float)