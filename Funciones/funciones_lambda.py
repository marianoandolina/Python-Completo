"""Funciones lambda"""
""" 
Las principales caracteristicas de las funciones lambda son:

---> Son creadas para ahorrar lineas de codigo, para usar menos bloques de memoria
---> Realizan el return de manera automatica
---> No son aptas cuando tenemos que realizar mas de una instruccion
"""


# basicamente es como crear una funcion anonima
# creamos la funcion con el nombre "multiplicar_por_2"
multiplicar_por_2 = lambda x: x * 2

print("-------------------------------------------------")
print("Funciones lambda")
print()
# usando la funcion
# retorna el numero pasado por parametro multiplicado por 2
print(multiplicar_por_2(5))  # muestra por consola 10}

"""
La funcion lambda que vimos arriba:

multiplicar_por_2 = lambda x : x*2 

Es igual a hacer lo siguiente:

def multiplicar_por_2(x):
    return x*2

"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# creando una funcion comun para verificar si un numero es par o no


def es_par(num):
    if num % 2 == 0:
        return True


"""Usando filter con una funcion comun
--> Sirve para usar una funcion que retorne True o False
--> Crea una lista para todos los valores en que la funcion retorno true
--> Es como hacer un bucle ficticio
"""

# con la siguiente linea le indicamos que aplique la funcion es_par a todos los elementos de la lista numeros
# nos retorna uno ojeto que podemos transformar en lista

numeros_pares = filter(es_par, numeros)  # retorna un objeto

print("-------------------------------------------------")
print("Funcion filter")
print()

print(numeros_pares)  # muestra el objeto filter object
# muestra la lista de numeros que son pares
# es como hacer un bucle ficticio, le aplica la funcion a cada elemento de la lista
# nos retorna un objeto filter y al transformarlo en lista vemos la lista de los numeros pares en este caso
print("-------------------------------------------------")
print("El mismo ojeto filter de arriba ahora hecho lista")
print()
print(list(numeros_pares))

"""Creando lo mismo que antes pero con la funcion lambda"""

numeros_pares_2 = filter(lambda numero: numero % 2 == 0, numeros)
print("-------------------------------------------------")
print("Lo mismo que antes pero con la funcion lambda")
print()
# retorna lo mismo que antes pero ahora realizado con la funcion lambda
print(list(numeros_pares_2))
