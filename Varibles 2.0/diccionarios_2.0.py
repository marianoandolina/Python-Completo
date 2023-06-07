'''DICCIONARIOS'''

# creando diccionario con dict
# tenemos que pasarle la clave y el valor de esta manera

diccionario = dict(nombre='oriana', apellido='andolina',
                   profesion='estudiante')
print(diccionario)
print("---------------------")
# las listas no pueden ser claves ni conjuntos (set)

try:
    # si lo dejamos asi nos tira error, para ver el error quitar el try y el except
    diccionario1 = {['dalto', 'palto']: 'ahora'}
    print(diccionario1)
except:
    print('El diccionario no puede contener listas como claves')
    print("---------------------")

# usamos frozenset para poner un conjunto como clave
diccionario3 = {frozenset(['dalto', 'palto']): 'ahora'}
print(diccionario3, type(diccionario3))
print(diccionario3[frozenset(['dalto', 'palto'])])
print("---------------------")

# creando diccionarios con el metodo fromkeys con la siguiente estructura dicr.fromkeys(["clave","clave","clave"])
# esta funcion nos permite el diccionario con todas las claves peros sin los valores

# crea el diccionario con todas las claves que les pasamos pero con el valor None
diccionario4 = dict.fromkeys(["nombre", "apellido", "edad"])
# muestra clave:None, clave:none, clave:none
print(diccionario4, type(diccionario4))
print("---------------------")

# otra manera de crear un diccionario con dict.fromkeys()
# le pasamos los datos por parametro pero no en forma de lista

# al pasarle un iterable por parametro toma cada caracter como clave y le asigna el valor None
# ej: 'M':None, 'a':None, 'r':None etc
diccionario5 = dict.fromkeys('Mariano')
print(diccionario5, type(diccionario5))
print("---------------------")

# y si le pasamos de la siguiente manera vemos lo que ocurre
# a cada caracter de la palabra 'hola' le asigna el valor 'chau'
diccionario6 = dict.fromkeys('hola', 'chau')
print(diccionario6, type(diccionario6))
print("---------------------")

# tambien podemos pasarle una lista como value o valor
# a los valores pasados por lista como parametro 1 les asigna lo que le pasamos como parametro 2
diccionario7 = dict.fromkeys(['river', 'boca'], 'grande')
# retorna el diccionario {'river': 'grande', 'boca': 'grande'}
print(diccionario7)
print("---------------------")
