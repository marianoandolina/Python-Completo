'''
Son datos que adentro tiene datos simples u otros datos compuestos pero 
que podemos agruparlos
'''

# Las listas son un tipo de dato compuesto

# Creamos una lista
# Esta lista contiene 3 elementos.
mariano = ['40 años', '183 de altura', 'Argentino']
print(mariano)  # Muestra la lista mariano
# Para contar los elementos de la lista usamos la funcion len
print(len(mariano))  # Muestra 3
# Los elementos de la lista se empiezan a contar desde el 0.
# Para acceder a los elementos de la lista accedemos a traves del indice que es la posicion de cada elemento dentro de la lista

# Para acceder al primer elemento de la lista usamos los corchetes.
print(mariano[0])  # Muestra el primer elemento de la lista que seria '40 años'
print(mariano[1])  # Muestra el segundo elemento
print(mariano[2])  # Muestra el tercer elemento

# Para cambiar un elemento de la lista
mariano[0] = '41 anios'  # Ahora la posicion [0] es '41 anios'
print(mariano)  # Muestra la lista con la ultima modificacion que realizamos

# Tuplas

# Las tuplas son iguales que las listas pero con la diferencia que no se pueden modificar y que ponen con parentesis.

casa = ('mesa', 'cocina', 'comedor', 'techo')

print(casa)  # Muestra los elementos que componen la Tupla "casa"
print(type(casa))  # Muestra el tipo de dato almacenado en casa
print(type(mariano))  # Muestra el tipo de dato almacenado en mariano

# Para mostrar los elementos de las tuplas mediante el indice tambien usamos corchetes.

print(casa[0])  # Muestra el indice 0 de la tupla.

''' Set o conjunto

Es muy parecido a las listas pero se crea con llaves en vez de corchetes.
No puede haber datos duplicados. A diferencia de las listas y las tuplas.
Se puede iterar mediante un bucle pero no acceder a sus elementos mediante el indice.
'''


conjunto = {'mesa', 'cocina', 'comedor', 'techo'}
print(conjunto)

# Se puede modificar en su totalidad pero no por elementos separados.
conjunto = {'gato', 'perro', 'conejo', 'tucan'}
print(conjunto)

# Tampoco podemos acceder o mostrar sus elementos en forma individual.

# print(conjunto[0])  # Nos tira un error
print(conjunto)  # Nos devuelve el conjunto en su totalidad

# Iterando un set o conjunto con un bucle for

for x in conjunto:
    print(x)  # Muestra cada elemento de un conjunto

# Diccionario

diccionario = {
    'nombre': 'Mariano',
    'apellido': 'andolina',
    'edad': 40,
    'hobby': 'programar'
}
# Se almacena con clave:valor

# Muestra la cantidad de elementos del diccinario (4), cada clave y valor o key, values es un 1 elemento.
# Es como una lista donde clave:valor es 1 elemento, observemos como estan separados por comas.

print(len(diccionario))

# Accedemos a los elementos a traves de su clave
print(diccionario['nombre'])  # Nos devuelve 'Mariano'

# Devuelve el valor correspondiente a la clave edad y le suma 2 (42)
print(diccionario['edad'] + 2)
