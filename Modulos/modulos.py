#       MODULOS:
#        
#       Importamos el modulo_saludar, lo que nos va a permitir usar las funciones creadas en dicho modulo
#       Para usar las funciones dentro del modulo tenemos que usarlas como si fueran metodos, es decir con esa sintaxis             

# importar el modulo para usarlo con otro nombre que le asignemos
# import modulo_saludar as mosa 

# importamos el modulo completo
import modulo_saludar



# lo utilizamos dentro de la variable saludar
# ATENCION A LA SINTAXIS PARA USAR LA FUNCION
# el nombre correcto de decir lo que es le modulo_saludar es nombrarlo "name space"
saludo = modulo_saludar.saludar("Mariano")
print(saludo)

# tambien probamos con la otra funcion dentro del modulo
# el nombre que se le pome al modulo es "name space"
# el "name space" es modulo_saludar
# PRESTAR ATENCION A LA SINTAXIS
que_hago = modulo_saludar.compra_o_venta(50000)

#     IMPORTANDO SOLO LAS FUNCIONES O PARTES QUE NOS INTERESAN

#   Tambien podemos solo importar lo que queremos del modulo
#   Si lo importamos de la siguiente manera:

#   from modulo_saludar import saludar, compra_o_venta      # estamos importando cada funcion que queremos usar del modulo, por lo tanto la forma de usarlos cambia.

#   Podemos cambiarle el nombre a las funciones usando as
#   Ej: from modulo_saludar import saludar as sld # Le indicamos que en este archivo la funcion tendra ese nombre al momento de usarla

#   Cuando importamos las funciones de los modulos de esta manera, la forma correcta de llamarlos es la siguiente:

#   saludo = saludar("Mariano") # sin colocar el name space
#   print(saludo)

#   Lo mismo para la otra funcion que tenemos dentro de ese modulo

#   que_hago = compra_o_venta(50000)

#---------------------------------------------------------------------------------------------------#

# Para ver las propiedades y metodos del name space

print(dir(modulo_saludar))

# Para acceder al nombre original del modulo en el caso de que hallamos usado as para cambiarle el nombre con el que lo vamos a llamar

# print(sld.__name__) # nos retorna el verdadero nombre del modulo sld que seria en este caso saludar

# Accedemos al nombre de este modulo

print(__name__) # retorna __main__










