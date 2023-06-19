"""Funciones lambda"""
""" 
Las principales caracteristicas de las funciones lambda son:

---> Son denominadas funciones anonimas
---> Son creadas para ahorrar lineas de codigo, para usar menos bloques de memoria
---> Realizan el return de manera automatica
---> No son aptas cuando tenemos que realizar mas de una instruccion
---> Permiten pasar multiples argumentos
---> Solo permite una expresion, es decir una sola linea de codigo
---> Estructura : lambda arg1, arg2: expression
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

# Ejemplos de Funcines lambda (YouTube:Dimas)
# Estructura
suma = lambda a, b: a + b
# llamamos a la funcion, pasamos como argumentos 5 y 9
print(suma(5, 9))
# llamamos a la funcion, pasamos como argumentos 6 y 2
print(suma(6, 2))

# recive como argumento un nombre y muestra por consola el saludo utilizando ese nombre
saludar = lambda nombre: print(f"Hola {nombre} !!!")

print("-------------------------------------------------")
saludar("Mariano")
saludar("Oriana")

# HACEMOS UNA FUNCION LAMBDA PARA DEVOLVER EL NUMERO MAXIMO

#       En la variable maximo hacemos la function lambda con 3 parametros (a,b,c)
#       luego usamos la funcion max() dentro de la expresion para que nos devuelva el maximo
#       de esos 3 valores (a,b,c)

maximo = lambda a, b, c: print(f"El maximo entre {a}, {b} y {c} es {max(a, b, c)}")

print("-------------------------------------------------")
maximo(5, 78, 2)
maximo(8, 42, 23)

#       UTILIZANDO FUNCIONES LAMBDA DENTRO DE FUNCIONES CONVENCIONALES

#       Podemos utilizar las funciones lambda dentro de funciones convencionales.
#       Esto nos permite generar diversas funciones lambda con diversos parametros
#
#       Vamos a los ejemplos:

#       Generamos una funcion que crea una lambda
#       para poder ingresar distintos parametros


def poner_prefijo(prefijo):
    return lambda nombre: f"{prefijo} {nombre}"


#       Mediante estas variables fijamos el parametro "prefijo"

add_mr = poner_prefijo("Mr")
add_sr = poner_prefijo("Sr")
add_miss = poner_prefijo("Miss")

#       Cuando llamamos a la funcion le pasamos el "nombre" por parametro

print("-------------------------------------------------")
print(add_mr("Mariano"))
print(add_sr("Gabriel"))
print(add_miss("Francesca"))

#       Creamos una funcion para elevar un numero a un exponenete,
#       nos retorna una funcion lambda que realiza la cuenta.


def elevar_a(exponente):
    return lambda base: base**exponente


#       Fijamos el parametro "exponente"

elevar_cuadrado = elevar_a(2)
elevar_cubo = elevar_a(3)

#       Al llamar a la funcion le pasamos como parametro el "base"
print("-------------------------------------------------")
print(elevar_cuadrado(3))
print(elevar_cubo(2))
