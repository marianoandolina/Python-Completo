#       EJERCICIO 2.2
#
#       Creando una funcion que nos devuelva los numeros primos entre
#       cero y el numero que le indiquemos por parametro


# creamos una funcion que verifique si un numero es primo
def es_primo(num):
    # verificamos que el numero pasado no pueda dividirse
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return True


def primos_hasta(num):
    primos = []
    for i in range(3, num + 1):
        resultado = es_primo(i)
        if resultado == True:
            primos.append(i)
    return primos


if __name__ == "__main__":
    resultado = primos_hasta(100)
    print(resultado)
