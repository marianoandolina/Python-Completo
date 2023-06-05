diccionario = {
    'nombre': 'Mariano',
    'apellido': 'Andolina',
    'edad': 40
}

print(diccionario)

# KEYS

# Nos muestra las keys del diccionario en cuestion
# Tambien nos sirve para iterar los keys

print()
claves = diccionario.keys()
print(claves)

# GET

# Accedemos a los valores a traves de las keys
# Si nos equivocamos colocando el nombre de la clave no nos lanza error, simplemente nos devuelve None

print()
nombre = diccionario.get('nombre')  # Retorna Mariano
apellido = diccionario.get('apellido')  # Retorna Andolina
print(nombre, apellido)


# POP

# Elimina un elemento del diccionario
# Como parametro le pasamos la key de lo que queremos eliminar
# Borra key y value
# Podemos sacar varios elementos pasandolos como parametros separados por coma.


# Borrando 1 solo elemento
print()
diccionario.pop('nombre')
print(diccionario)

'''
Ejemplo para borrar varios elementos
Le pasamos por parametro de pop las keys separadas por coma

print()
diccionario.pop('nombre','apellido') #
print(diccionario)
'''

# ITEMS

# Obteniendo un elemto iterable
# Que es iterable significa que lo podemos recorrer cada item con un bucle for

print()
# Obtiene todos los items del diccionario
diccionario_iterable = diccionario.items()
print(diccionario)  # Mostramos el diccionario no iterable
print(diccionario_iterable)  # Mostramos el diccionario iterable

# CLEAR

# Elimina todo del diccionario
