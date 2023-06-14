"""Funcion para pasar varios parametros *args"""

# forma no optima de crear una funcion que suma valores


def suma_no_optima(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numero + numeros_sumados
    return numeros_sumados


print()
print("-----------------------------------------------")
print("Forma no optima de hacer una funcion para sumar")

resultado_1 = suma_no_optima([1, 2, 3])
print(resultado_1)

# forma correcta de hacer una funcion utilizando *args


# al colocar el * antes del parametro le estamos como indicando que le vamos a pasar una lista
def suma_optima(*numeros):
    return sum(numeros)


print()
print("-----------------------------------------------")
print("Forma optima de hacer una funcion para sumar")

resultado_2 = suma_optima(4, 5, 6)
print(resultado_2)

# forma correcta de pasarle otro parametro junto con *args
# pasandole otro parametro
# siempre el parametro *args tiene que ir ultimo


def suma_optima_2(nombre, *numeros):
    return f"({nombre}, la suma de tus numeros es {numeros})"


print()
print("-----------------------------------------------")
print("Pasando un parametro y *args")

# llamamos a la funcion y le pasamos los parametros
resultado_3 = suma_optima_2("Mariano", 3, 5, 6, 1)
# mostramos por consola el resultado
print(resultado_3)


# de esta forma utilizamos el *args dentro de la funcion
# el parametro que coloquemos aca tiene que estar dentro de una lista para que sea 1 solo parametro
def suma_optima_3(numeros):
    return sum([*numeros])


print()
print("-----------------------------------------------")
print("Forma optima de hacer una funcion para sumar pero con el * en el return")

resultado_4 = suma_optima_3([3, 5, 6, 1])
print(resultado_4)
