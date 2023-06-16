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
print("Forzando argumentos")
print()
print(frase_resultante_2)

"""Pasando argumentos ya definidos o por default"""

# creando la misma funcion con un parametro opcional y un valor por defecto
# el parametro opcional es "adjetivo" y el valor por defecto es "tremendo crack"
def frase_2(nombre, apellido, adjetivo="tremendo crack"):
    return f"Hola, {nombre} {apellido}, sos un {adjetivo}."

print("------------------------------------------------------")
print("Pasando argumentos ya definidos o por default")
print()
# vemos que en ningun momento le pasamos el valor de "adjetivo"
# pero lo coloca igual porque tiene un valor colocado por default dentro de los parametros de al funcion
frase_resultante_3 = frase_2("Mariano", "Andolina")
print(frase_resultante_3)

# podemos cambiar el valor por default se asi lo deseamos
print("------------------------------------------------------")
print("Cambiando el valor que viene por defaul")
print()
frase_resultante_4 = frase_2("Oriana", "Andolina", "inteligente")
print(frase_resultante_4)

