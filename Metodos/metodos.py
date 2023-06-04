'''
Las cadenas de textos o strings tienen sus propios metodos
Vamos a repasar los metodos de las cadenas
'''

cadena_1 = 'Hola, soy Mariano'
cadena_2 = 'Bienvenido maquinola'
lista_1 = ['Mariano', 'Oriana', 'Myrian']

# DIR (NO ES UN METODO, ES UNA FUNCION, POR ESO SE LE PASA EL PARAMETRO DENTRO DE LOS PARENTESIS)

# Nos muestra todo los metodos disponibles para realizar
# Podemos pasarle una variable que contenga, str, int, lista, tupla, diccionario etc y nos va a mostrar todos los metodos que correspondan a ese tipo de dato

print(dir(cadena_1)) # La cadena_1 es un str por lo tanto nos muestra los metodos para aplicar a uns str
print() # Solo para dejar un espacio entre el print de arriba y el de abajo
print(dir(lista_1)) # La lista_1 es una list por lo tanto nos muestra los metodos para aplicar a las listas

resultado = dir(cadena_1) # Guardamos la lista de metodos en una variable
# Realizamos un bucle for para que se vea un metodo debajo del otro en la consola, de manera mas sencilla de leer
# for x in resultado:
#    print(x)


# Metodos de las cadenas (PONER ATENCION EN LA SINTAXIS PARA UTILIZAR LOS METODOS)

# La sintaxis correcta es DATO.METODO()

# UPPER 

# Pone todo el str en mayusculas

print(cadena_1.upper()) # Muestra lo que esta guardado en la variable pero todo en mayuscula
mayus = cadena_1.upper() # Guarda en esta varible lo que esta en cadena_1 pero pasado todo a mayuscula
mayus2 = "hola todos, como estan".upper() # Transforma todo en mayusculas el str que precede al punto y lo guarda en la variable
print(mayus)
print(mayus2)

# LOWER

# Pone todo en minusculas

print(cadena_1.lower()) # Muestra lo que esta guardado en la variable pero todo en minusculas
mayus = cadena_1.lower() # Guarda en esta varible lo que esta en cadena_1 pero pasado todo a minusculas
mayus2 = "hola todos, como estan".lower() # Transforma todo en minusculas el str que precede al punto y lo guarda en la variable
print(mayus) 
print(mayus2)

# CAPITALIZE

# Pone la letra de cada palabra en Mayuscula

print(cadena_1.capitalize()) # Muestra lo que esta guardado en la variable pero con la primera letra del str en Mayuscula 
mayus = cadena_1.capitalize() # Guarda en esta varible lo que esta en cadena_1 pero con la primera letra del str en mayuscula
mayus2 = "hola todos, como estan".capitalize() # Transforma la primera letra del str que precede al punto en mayuscula y lo guarda en la variable
print(mayus)
print(mayus2)













