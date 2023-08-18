#       ABSTRACCION

#       Significa manejar la complejidad ocultando todos los detalles innecesarios al usuario o al programador y dandole solo las funcionalidades relevantes
#       No necesitas saber como funciona internamente si no que solamente tenes que saber como usarlo
#       Basicamente es ocultar la complejidad de un sistema

# ej:


class Auto:
    def __init__(self):
        self._estado = "apagado"

    def encender(self):
        print("El auto esta encendido")

    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo el auto")


mi_auto = Auto()
mi_auto.conducir()

"""En este ejemplo es una abstraccion porque el usuario solo aplica la funcion conducir pero no tiene idea lo que esta ocurriendo dentro de la funcion,
por ejemplo que la funcion verifica si el auto esta encendido y de no ser asi lo enciende para empezar a conducir, el usuario solo usa la funcion y esta
abstraido de todo lo que ocurre al momento de ejecutarla
"""
