ingreso_mensual = 100000

if ingreso_mensual > 1000:
    print ("Estas bien economicamente")
if ingreso_mensual > 10000:
    print ("No tienes que preocuparte por tu economia")
else:
    print("eres pobre")
#Pero si quiero que solo me diga una cosa 
#yo no quiero que me diga dos cosas
#solo quiero una cosa en concreta
#porque si ponemos a (ingreso_mensual = 5000)
#el codigo me dira "estas bien economicamente" 
# y tambien dira "eres pobre"
#Para que no nos salga eso en el codigo trabajamos con 
#"else if" pero en python se escribe "elif"
if ingreso_mensual > 10000:
    print("No tienes que preocuparte por tu economia")
elif ingreso_mensual > 1000:
    print("estas bien economicamente")
elif ingreso_mensual > 500:
    print("tu economia esta normal")
elif ingreso_mensual > 200:
    print("tu economia esta baja")
else:
    print ("eres pobre")
#asi se trabajaria con un elif 

#Tambien tenemos los if anidados que es un if adentro de otro if
#Cuando se usas este if anidados, supongamos que tuvieramos que cumplir
#dos condiciones al mismo tiempo podemos usar un if anidados
#por ejemplo:
Ingreso = 100000
gasto = 800000

if Ingreso > 10000:
    if Ingreso - gasto <0:
        print("estamos en deficit")
    elif Ingreso - gasto > 30000:
        print("estamos bien economicamente")
    else:
        print("estas gastando mucho")