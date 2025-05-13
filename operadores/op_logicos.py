#AND 
#Esto es un operador que compara el uno y otro
Resultado = True & True #DEVUELVE TRUE
Resultado1 = False & True #DEVUELVE FALSO
Resultado2 = True & False #DEVUELVE FALSO
Resultado3 = False & False #DEVUELVE FALSO

#OR
#ESTE OPERADOR NOS DEVUELVE FALSO SI AMBAS CONDICIONES NO SE CUMPLEN
Resultado5 = True | True #DEVUELVE TRUE
Resultado6 = False | True #DEVUELVE TRUE
Resultado7 = True | False #DEVUELVE TRUE
Resultado8 = False | False #DEVUELVE FALSO

#NOT
#ESTE OPERADOR NOS INVIERTE EL VALOR, SI LE DAMOS UN VALOR TRUE
#LO CONVIERTE A UNO FALSO OSEA FALSE LO MISMO VICEVERSA
Resultado9 = not True # DEVUELVE FALSO
Resultado10 = not False # DEVUELVE TRUE

print(Resultado7)