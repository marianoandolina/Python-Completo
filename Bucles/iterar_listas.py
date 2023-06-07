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

print('-------------------------------------')

# realizamos un bucle con numeros que realiza una multiplicacion en cada vuelta
# creamos una lista con numeros
numeros = [52, 16, 14, 72]

# bucle
for numero in numeros:
    # a cada numero de la lista lo multiplicamos por 10
    resultado = numero * 10
    # mostramos por pantalla el resultado
    print(resultado)

print('-------------------------------------')

'''FUNCION zip()'''

# podemos iterar dos listas juntas
# para realizar esto tenemos que tener listas que contengan la misma cantidad de elementos

print('Funcion zip()')
print()
for numero, animal in zip(numeros, animales):
    print(f'Recorriendo lista 1: {numero}')
    print(f'Recorriendo lista 2: {animal}')

print('-------------------------------------')

'''FUNCION range()'''

print('Funcion range()')
print()

# si le ponemos un parametro solo a range() va desde cero hasta ese parametro
# si le ponemos 2 parametros arranca con el primero y termina 1 numero menos que el segundo
# si le ponemos 3 parametros, el ultimo es de cuanto en cuanto
# para cada numero en el rango de 5 a 11 (el 11 no esta incluido) hace lo siguiente
for num in range(5, 11):
    # muestra el numero guardado en la variable en cada vuelta
    print(num)

print('-------------------------------------')

# forma no optima de recorrer una lista
print('Forma no optima de recorrer una lista con range()')
print()

for num in range(len(numeros)):
    print(numeros[num])

print('-------------------------------------')

# forma correcta de recorrer una lista con su indice

print('Forma correcta de recorrer una lista por su indice')
print('Funcion enumerate()')
print()

for num in enumerate(numeros):
    print(numeros[num])
