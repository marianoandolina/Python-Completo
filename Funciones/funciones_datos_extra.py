def frase(nombre, apellido, adjetivo):
    return f"Hola, {nombre} {apellido}, sos muy {adjetivo}"


# estos parametros se llaman parametros de posicion

frase_resultante = frase("Mariano", "Andolina", "Crack")
print("------------------------------------------------------")
print()
print(frase_resultante)


"""Forzando argumentos"""
# de esta forma puedo poner los argumentos de la maneraque yo quiera
# si coloco un argumento de esta manera tengo que colocar todos de la misma manera
# no puedo hacer lo siguiente --> frase_resultante_2 = frase("Martin", adjetivo="Capo","Andolina")
# estos parametros se llaman keywords parameters

frase_resultante_2 = frase(nombre="Martin", adjetivo="Capo", apellido="Garcia")
print("------------------------------------------------------")
print()
print("Forzando argumentos")
print(frase_resultante_2)

"""Pasando argumentos ya definidos o por default"""


def frase_2(nombre, apellido, adjetivo="tremendo crack"):
    return f"Hola, {nombre} {apellido}, sos un {adjetivo}."


frase_resultante_3 = frase_2("Mariano", "Andolina")
print("------------------------------------------------------")
print()
print("Pasando argumentos ya definidos o por default")
print(frase_resultante_3)
