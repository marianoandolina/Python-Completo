''' UN BUCLE ES REPETIR DE UNA FORMA CONTROLADA LA EJECUCION DE UN CODIGO'''

'''
ITERAR

Iterar es recorrer un elemento en partes

Los elementos iterables son:

listas, diccionarios, tuplas, cadenas de textos, conjuntos 

'''

# bucle for

# el bucle se va a ejecutar la cantidad de veces igual a la cantidad de elementos a recorrer
# python crea una variable que va a guardar cada parte que valla iterando el bucle

# creamos una lista
animales = ['perro', 'gato', 'loro', 'cocdrilo']

# iteramos con un bucle for
# para cada vuelta que de el bucle agarra un elemento y lo guarda en la variable animal que es temporal
for animal in animales:
    print(animal)


for animal in animales:
    # podemos hacer el print asi para que veamos cada vuelta
    print(f'Ahora la variable animal es igual a: {animal}')


# realizamos un bucle con numeros que realiza una multiplicacion en cada vuelta
# creamos una lista con numeros
numeros = [52, 16, 14, 72]

# bucle
for numero in numeros:
    # a cada numero de la lista lo multiplicamos por 10
    resultado = numero * 10
    # mostramos por pantalla el resultado
    print(resultado)
