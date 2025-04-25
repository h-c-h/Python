igual_que = 5 == 6 #->false
#El primer igual estamos asignando, estamos diciendo que la variable
#"es_igual_que" va a ser igual a el valor que pongamos.
#Ahora si quermos comparar usamos dos iguales
distinto_de = 5 !=6 #-> true

mayor_que = 5 > 6#->false

menor_que = 5 < 6#->true

mayor_o_igual = 5 >= 6# ->false

menor_o_igual = 5 <= 6# ->true

#Si se cumple la propiedad es verdadera no pondra True, si es falsa False

print(igual_que)
print(distinto_de)
print(mayor_que)
print(menor_que)
print(mayor_o_igual)
print(menor_o_igual)


#Calculos combinados
a = 5
b = 10
c = 20
comparacion = a + b < c

print(comparacion)


#comparar usuarios

contraseña_almacenada = "JuanZavala"
contraseña_escrita = "Juan"
print(contraseña_almacenada == contraseña_escrita) #-> Esta parte nos
#tira false porque no son iguales


usuario_almacenado = "Zavala"
usuario_escrito = "Zavala"
print(usuario_almacenado == usuario_escrito)#-> Esta parte nos 
#tira true porque si son iguales

