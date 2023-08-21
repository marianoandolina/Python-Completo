# LSP
# La clase que hereda tiene que poder hacer todo lo mismo de la clase que hered


# El codigo escrito de la siguiente manera no respeta el rincipio LCP porque la clase Pinguino no puede volar y la clase padre Ave si puede
# Es decir todo lo que la clase puede hacer, tambien tiene que poder hacerlo la subclase
# En el ejemplo siguiente el pinguino no vuela, cosa que la clase padre si hace, entonces no se esta respetando el principio de LSP.
# El codigo se encuentra comentado para que solo sea a modo de ejemplo.

# >>>
# class Ave:
#     def volar(self):
#         return "Estoy volando"


# class Pinguino(Ave):
#     def volar(self):
#         return "No puedo volar"


# def hacer_volar(ave=Ave):
#     return ave.volar()


# print(hacer_volar(Pinguino()))

# Ejemplo de como tendria que ser el codigo mismo codigo anterior pero respetando el principio LSP


class Ave:
    pass


class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"


class AveNoVoladora(Ave):
    pass
