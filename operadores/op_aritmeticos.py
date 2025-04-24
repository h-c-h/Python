#suma y resta (+ y -)
suma = 12 + 5
resta = 12 - 5


#multi y división (* y /)
multi = 12 * 5
division = 12 / 6 #->devuelve un dato float(flotante)

#potenciación (exponente) (**)
exponente = 12**2

#división baja (//)
division_baja = 12 // 5 # ->devuelve un dato entero redondeado hacia abajo
#¿por qué? duelve entero, esto se debe a que en la division baja 
#lo que está depués de la coma lo borra es decir en la division
#12//5 es 2.4 borraria el 4 y lo convierte en un enterio lo redondea
#hacia abajo, no importa si es 5,999999 igual lo borra y lo redondea
#hacia abajo

#resto o módulo 
resto = 12 % 5 
#En el resto nos muesta cuanto no sobra en la división
#osea de la divión -12/5
#                   10 2
#                    2   <- esto viene hacerl el resto
resto2 = 12 % 7
#otro ejemplo seria -12/7
#                     7 1
#                     5   <- el resto vendria hacer 5
print(suma)
print(resta)
print(multi)
print(division)
print(exponente)
print(division_baja)
print(resto)
print(resto2)

#funcion para ver el tipo de dato "type"
tipo_de_dato = type(division_baja)
print(tipo_de_dato)