"""Creando una funcion simplre"""

# se coloca la palabra def al comienzo y luego el nombre de la funcion y los parentesis

print()
print("---------------------------------------")
print()


def saludar():
    print("Hola Mariano, como andas")


# llamamos a que se ejecute la funcion
saludar()  # retorna lo que le pedimos dentro de la funcion

"""Creando funcion que tenga parametro"""

# los parametros son variables que se crean para ser usadas dentro de la funcion
# creamos otra funcion para saludar, entre parentesis le ponemos un nombre al parametro que va a recibir


def saludo2(
    nombre,
):  # el nombre de la variable donde se va a guardar el parametro es "nombre"
    print(
        f"Hola {nombre}, como estas"
    )  # usamos un f str para pasarle la variable donde esta guardado el parametro a utilizar


print()
print("---------------------------------------")
print()

# pasamos el parametro dentro de los parentesis
saludo2("Mariano")

"""Funcion con 2 parametros"""

# esta funcion es la misma que saludar pero recive 2 paramtros, nombre y sexo


def saludo3(nombre, sexo):
    # tomamos la variable sexo y le aplicamos el metodo lower()
    sexo = sexo.lower()
    # usamos if - elif para verificar si
    # el parametro pasado en sexo es mujer, hombre u otro
    if sexo == "mujer":
        # si el parametro pasado es "mujer" la varible adjetivo tiene este valor
        adjetivo = "genia"
    elif sexo == "hombre":
        # si el parametro pasado es "hombre" la varible adjetivo tiene este valor
        adjetivo = "titan"
    else:
        # si el parametro pasado es otroñ la varible adjetivo tiene este valor
        adjetivo = "amor"

    print(f"Hola {nombre}, mi {adjetivo}, como estasss?")


print()
print("---------------------------------------")
print()

saludo3("Mariano", "hombre")

"""Retornando valores en una funcion

Cuando usamos print() para terminar la funcion nos muestra el valor por pantalla y la funcion termina alli,
no podemos hacer nada con ese valor que muestra por pantalla.

Cuando usamos return podemos guardar para usar y trabajar con ese valor que retorno la funcion, veamos un ejemplo

"""

# crear una funcion que nos retorne valores


# esta funcion recibe un numero por parametro
def crear_contraseña(num):
    # creamos una varible que contenga caracteres que van a ser utilizados en esa contraseña
    chars = "abcdefghi"
    # transformamos el numero ingresado por parametro en un str
    num_entero = str(num)
    # nos quedamos con el primer numero ingresado como parametro
    num = int(num_entero[0])
    # con el numero ingresado creamos numeros que vamos a usar como indice al momento de crear la contraseña
    c1 = num + 2
    c2 = num - 4
    c3 = num
    # creamos la contraseña
    # en esta varible pasamos la varible chars con el indice que es otra varible creada anteriormente
    # el indice tiene que ser un int siempre
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*4}"
    # retornamos la contraseña
    return contraseña


print()
print("---------------------------------------")
print("La contraseña creada con la funcion es: ")

contraseña = crear_contraseña(5)
print(contraseña)

"""Podemos crear una funcion que nos retorne multiples valores"""


def crear_contraseña_2(num):
    # creamos una varible que contenga caracteres que van a ser utilizados en esa contraseña
    chars = "abcdefghi"
    # transformamos el numero ingresado por parametro en un str
    num_entero = str(num)
    # nos quedamos con el primer numero ingresado como parametro
    num = int(num_entero[0])
    # con el numero ingresado creamos numeros que vamos a usar como indice al momento de crear la contraseña
    c1 = num + 2
    c2 = num - 4
    c3 = num
    # creamos la contraseña
    # en esta varible pasamos la varible chars con el indice que es otra varible creada anteriormente
    # el indice tiene que ser un int siempre
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*4}"
    # retornamos la contraseña y el numero que usamos para crearla
    return contraseña, num


print()
print("---------------------------------------")
print()

# desempaquetamos los valores que retorna la funcion en 2 variables
password, primer_numero = crear_contraseña_2(516)
# mostramos por consola la contraseña
print(f"La contraseña creada es {contraseña}")
# mostramos por consola el numero usado para crear la contraseña
print(f"El numero que se uso para crearla fue el {primer_numero}")

print("---------------------------------------")
