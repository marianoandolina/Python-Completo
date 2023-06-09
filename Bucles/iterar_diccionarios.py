diccionario = {
    'nombre': 'Mariano',
    'apellido': 'Andolina',
    'subs': 1000000
}

print(diccionario)

# recorriendo un diccionario
# realizando un for simple de esta manera nos muestra solo las keys
print("----------------------------")
print('Recorriendo un diccionarioa de manera simple')
print()

for key in diccionario:
    # nos devuelve las claves del diccionario
    print(key)

print('----------------------------')

'''Recorriendo un diccionario con Items'''

print('Usando .items()')
print()

# Cuando usamos .items nos devuelve clave y valor en cada vuelta en forma de tupla
for key in diccionario.items():
    key
    print(key)

# Podemos acceder a la clave y el valor de la siguiente manera

print('----------------------------')
for datos in diccionario.items():
    key = datos[0]
    Value = datos[1]
    print(f"La clave es: {key} y el valor es: {Value}")
print('----------------------------')
