'''
Los operadores de pertenencia son 

in, not in

Un operador de pertenencia se emplea para identificar pertenencia en alguna secuencia (listas, strings, tuplas).

in devuelve True si el valor especificado se encuentra en la secuencia. En caso contrario devuelve False.

not in devuelve True si el valor especificado no se encuentra en la secuencia. En caso contrario devuelve False.

'''

# EJEMPLOS

a = [1, 2, 3, 4, 5]

# Esta 3 en a
print(3 in a)  # Devuelve True
# Esta 8 en a
print(8 in a)  # Devuelve False
# Aca le digo que 3 no esta en a.
print(3 not in a)  # Nos devuelve False porque 3 si esta en a.
