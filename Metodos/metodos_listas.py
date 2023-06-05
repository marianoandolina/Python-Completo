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
# Recordamos que el indice en la lista empieza desde el cero
# El indice negativo empieza desde atras de la lista en -1

print()
print(lista) # Muestra la lista antes del pop
lista.pop(0)
print(lista) # Muestra la lista depues de que pop elimino el elemento 0

# REMOVE

# Remueve un elemento de la lista por su valor
# Si lo encuentra lo elimina y si no lamza una excepcion

print()
print(lista)
lista.remove(2030)
print(lista)

# SORT

# Ordena los elementos de forma ascendente (menor a mayor) siempre que sean todos numericos o todos str
# En el caso de que halla numeros y palabras en la lista para que sort funcione, los numeros tienen que estar escritos como str o sea entre comillas

print()
lista_numerica = [205,356,189,56,25,69]
print(lista_numerica)
lista_numerica.sort()
print(lista_numerica)

# Podemos revertir la lista si le pasamos por parametro reverse

print()
lista_numerica.sort(reverse=True) # Cambia el ordenamiento de la lista de ascendente a descendente
print(lista_numerica)

# REVERSE

# Invierte los elementos en el orden que esten

print()
lista_mezclada = [4,6,2,1,9]
print(lista_mezclada) # Muestra la lista como esta
lista_mezclada.reverse() # Muestra la lista al reves
print(lista_mezclada)

# CLEAR

# Elimina todos los elementos de la lista

print()
print(lista)
lista.clear()
print(lista)


 
 








