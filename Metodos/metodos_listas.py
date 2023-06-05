"""METODOS DE LISTAS"""

# LIST

# Crear una lista con list
# Para mi no tiene mucho sentido pero dalto lo mostro asi y dijo lo mismo

lista = list(['Mariano', 'Oriana', 'Tomy'])
print(list)

# LEN (Funcion)

# Retorna la cantidad de elementos de una lista

print()
resultado = len(lista)
print(resultado)

# APPEND

# Agrega elementos a la lista

print()
print(lista)
lista.append('Diamante')
print(lista)

# INSERT

# Tambien agrega un elemeto a la lista pero en un indice o index especifico que le pasamos nostros

print()
lista.insert(0, 'Sol')
print(lista)

# EXTEND

# Agrega varios elementos a la lista, no solo uno
# Los agrega al final de la lista

print()
lista.extend([2030, 'Argentina']) # Los parametros se pasan en forma de una lista ['Mariano','Tomas','Cristina']
print(lista)

# POP

# Elimina un elemento de la lista por su indice o index

print()
print(lista) # Muestra la lista antes del pop
lista.pop(0)
print(lista) # Muestra la lista depues de que pop elimino el elemento 0








