diccionario = {
    'nombre':'Mariano',
    'apellido':'Andolina',
    'edad':40
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
nombre = diccionario.get('nombre') # Retorna Mariano
apellido = diccionario.get('apellido') # Retorna Andolina
print(nombre, apellido)

# CLEAR

# Elimina todo del diccionario




