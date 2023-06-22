#       EJERCICIO 2.2
#
#       Creando una funcion que nos devuelva los numeros primos entre
#       cero y el numero que le indiquemos por parametro


# creamos una funcion que verifique si un numero es primo
def es_primo(num):
    # verificamos que el numero pasado no pueda dividirse por ningun numero
    # entre 2 y ese mismo numero -1

    for i in range(2, num - 1):
        # si es divisible por alguno retorna False y termina el bucle
        if num % i == 0:
            return False
    # si termina el bucle significa que no fue divisible, entonces es primo
    return True

# creamos una funcion que retorna una lista con todos los primos hasta cierto rango
def primos_hasta(num):
    # creamos la lista
    primos = []
    for i in range(3, num + 1):
        # verificamos si el valor es primo
        resultado = es_primo(i)
        if resultado == True:
            # si el valor es primo lo agregamos a la lista y si no es primo no hace nada
            primos.append(i)
    # retornamos la lista con todos los numeros primos
    return primos


if __name__ == "__main__":
    # creamos el resultado llamando a la funcion
    resultado = primos_hasta(100)
    # mostramos el resultado
    print(resultado)
