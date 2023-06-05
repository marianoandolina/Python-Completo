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

# La cadena_1 es un str por lo tanto nos muestra los metodos para aplicar a uns str
print(dir(cadena_1))
print()  # Solo para dejar un espacio entre el print de arriba y el de abajo
# La lista_1 es una list por lo tanto nos muestra los metodos para aplicar a las listas
print(dir(lista_1))

resultado = dir(cadena_1)  # Guardamos la lista de metodos en una variable
# Realizamos un bucle for para que se vea un metodo debajo del otro en la consola, de manera mas sencilla de leer
# for x in resultado:
#    print(x)


# Metodos de las cadenas (PONER ATENCION EN LA SINTAXIS PARA UTILIZAR LOS METODOS)

# La sintaxis correcta es DATO.METODO()

# UPPER

# Pone todo el str en mayusculas

# Muestra lo que esta guardado en la variable pero todo en mayuscula
print(cadena_1.upper())
# Guarda en esta varible lo que esta en cadena_1 pero pasado todo a mayuscula
mayus = cadena_1.upper()
# Transforma todo en mayusculas el str que precede al punto y lo guarda en la variable
mayus2 = "hola todos, como estan".upper()
print(mayus)
print(mayus2)

# LOWER

# Pone todo en minusculas

# Muestra lo que esta guardado en la variable pero todo en minusculas
print(cadena_1.lower())
# Guarda en esta varible lo que esta en cadena_1 pero pasado todo a minusculas
minus = cadena_1.lower()
# Transforma todo en minusculas el str que precede al punto y lo guarda en la variable
minus2 = "hola todos, como estan".lower()
print(minus)
print(minus2)

# CAPITALIZE

# Pone la letra de cada palabra en Mayuscula

# Muestra lo que esta guardado en la variable pero con la primera letra del str en Mayuscula
print(cadena_1.capitalize())
# Guarda en esta varible lo que esta en cadena_1 pero con la primera letra del str en mayuscula
capi = cadena_1.capitalize()
# Transforma la primera letra del str que precede al punto en mayuscula y lo guarda en la variable
capi2 = "hola todos, como estan".capitalize()
print(capi)
print(capi2)

# FIND

# Busca una cadena en otra cadena

# Busca la letra a dentro del str que esta en cadena_1 y nos retorna el indice donde se encuentra
# Nos devuelve -1 cuando no encuentra el valor
# Python es case sensitive o sea qu ojo con las mayusculas y minusculas
# Los espacios cuentan como caracter, tienen index tambien

busqueda_find = cadena_1.find('a')
print(busqueda_find)  # Retorna 3 porque la letra a esta en la posicion 3

# INDEX

# Igual a find
# Si no encuentra nada lanza una excepcion a diferencia de find

busqueda_index = cadena_1.index('a')
print(busqueda_index)  # Retorna 3 porque la letra a esta en la posicion 3

# ISNUMERIC

# Si es numerico devuelve True, de lo contrario devuelve False
# Tambien devuelve True si es un texto que tiene solo numeros

es_numerico = cadena_1.isnumeric()
print(es_numerico)

# ISALPHA

# Verifica si contiene numeros y letras, de lo contrario devuelve False
# Los espacios no son tomados como alphanumericos, por lo tanto si hay espacios en el texto devuelve False


es_alphanumerico = cadena_1.isalpha()
print(es_alphanumerico)

# COUNT

# Cuenta cuantas coincidencias hay del valor pasado por parametro dentro de una cadena determinada, devuelve la cantidad de coincidencias
# Cuenta exactamente el texto pasado por parametro sea una letra o una palabra

cout = cadena_1.count('a')
print(cout)

# LEN (Funcion)

# La funcion len cuenta cuantos caracteres tiene una cadena, incluyendo espacios

len = len(cadena_1)
print(len)

# STARTSWITH

# Verifica que la cadena empiece con el o los caracteres que le indicamos por parametro
# Recordamos que Python es case sensitive, por lo tanto reconoce minusculas de mayusculas

empieza_con = cadena_1.startswith('h')  # Devuelve False
print(empieza_con)

# ENDSWITH

# Verifica que la cadena termine con el o los caracteres que le indicamos por parametro
# Recordamos que Python es case sensitive, por lo tanto reconoce minusculas de mayusculas

termina_con = cadena_1.endswith('o')  # Devuelve True
print(termina_con)

# REPLACE 

# Reemplaza una parte de la cadena por otra, ambas son pasadas como parametro

# Al metodo replace, le pasamos como primer parametro la parte de la cadena que queremos reemplazar y como segundo parametro con que la vamos a reemplazar
# Si no encuentra el primer parametro en la cadena
cadena_nueva = cadena_1.replace('Hola', 'Chao')
print(cadena_nueva)

# SPLIT

# Separa la cadena como una lista
# Este metodo es el unico de todos los que tenemos aqui que nos devuelve una lista
# Una vez aplicado el metodo a la cadena podemos trabajar esta cadena como una lista
# Separa por cada espacio y no por cada caracter
# No toma los espacios como caracter

print(type(cadena_1)) # Vemos que tipo de dato es cadena_1, devuelve 'str'
split = cadena_1.split() # Usamos el metodo split para separar la cadena y guardarla en la variable split
print(split) # Muestra la variable split 
print(type(split)) # Muestra que tipo de dato es split, devuelve 'list'





