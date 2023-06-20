#       EJERCICIOS PRACTICOS 2
#
#       Lo primero que tenemos que hacer es anotar los datos, SIEMPRE ANOTAR LOS DATOS PRIMERO.

#       Falto el profe y los pibes van a armar la clase, el de mayor edad sera el profesor
#       y el de menor edad sera el ayudante.


# funcion para obtener el profesor y el asistente segun la edad
def obtener_compañero(cantidad_de_compañeros):
    # creando la lista de companieros
    compañeros = []  # hacemos la lista

    # ejecutando el for que pide la informacion de cada companiero
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingresa tu edad: "))

        # crea una tupla con el nombre y edad de cada companiero
        compañero = (nombre, edad)

        # agregamos a la lista cada una de las tuplas con el nombre y la edad
        compañeros.append(compañero)

    # ordenando la lista de menor a mayor con una funcion lambda
    compañeros.sort(key=lambda x: x[1])

    # compañeros[x] nos devuelve una de las tuplas (nombre,edad)
    # despues accdemos al nombre para guardarlo en la variable
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]

    # retornamos las variables en forma de tupla
    return asistente, profesor


if __name__ == "__main__":
    # desempaquetamos las variables
    asistente, profesor = obtener_compañero(4)

    # mostramos por consola las variables desempaquetadas
    print(f"El profesor sera {profesor} y su asistente sera el alumno {asistente}")
