#       DECORADORES

#       Es un concepto que es facil pero parece algo avanzado.
#       Es una funcion especial que decora a otra.
#       Toma una una funcion como entrada, le agrega una funcionalidad extra y la devuelve como salida.
#       Son utilizado para el manejo de excepciones, validacion de entradas, etc.


# la funcion decoradora hace lo siguiente:
def decorador(funcion):
    # crea una funcion
    def funcion_modificada():
        # que primero ejecuta un codigo antes
        print("Antes de llamar a la funcion")

        # ejecuta la funcion que le pasamos antes
        funcion()

        # luego ejecuta mas codigo
        print("Despues de llamar a la funcion")

    # por ultimo nos devuelve la funcion que creo pero sin ejecutar (sin parentesis)
    return funcion_modificada


# def saludo():
#     print("Hola Dalto")


# saludo_modificado = decorador(saludo)
# saludo_modificado()

# MODO CORRECTO DE CREAR DECORADORES.


@decorador  # nombre del decoradro
# funcion que le vamos a pasar para decorar
def saludo():
    print("Hola Dalto")


# funcion ya decorada
saludo()
