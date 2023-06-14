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

# forma correcta de hacer una funcion que sume varios parametros


# al colocar el * antes del parametro le estamos indicando que es una lista
def suma_optima(*numeros):
    return sum(numeros)


print()
print("-----------------------------------------------")
print("Forma no optima de hacer una funcion para sumar")

resultado_2 = suma_optima(4, 5, 6)
print(resultado_2)
