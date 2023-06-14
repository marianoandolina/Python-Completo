"""Funciones built in, es decir que ya estan creadas en Pyhton"""

"""max"""

# encontrando el numero mayor de una lista, tupla o conjunto

print()
print("----------------------------------")
print("Funcion max()")
numeros = [4, 7, 1, 42, 15]
numero_mas_alto = max(numeros)
print(numero_mas_alto)

"""min"""

# encontrando el numero menor de una lista

print()
print("----------------------------------")
print("Funcion min()")
numeros = [4, 7, 1, 42, 15]
numero_mas_alto = min(numeros)
print(numero_mas_alto)

"""round()"""

# redondeando a la cantidad de decimales elegidos
# colocamos la funcion, como primer parametro el numero a redondear y como segundo parametro la cantidad de decimales que queremos que tenga

# redondeamos a 2 decimales despues de la coma
print("----------------------------------")
print("Funcion round()")

numero = round(12.345678, 2)
print(numero)

# redondeamos a 4 decimales despues de la coma
numero = round(12.345678, 4)
print(numero)

"""Funcion bool()"""

# retorna False cuando le pasamos 0, vacio, False, None
# retorna True cuando le pasamos distinto a cero, True, cadena, datos no vacios

print("----------------------------------")
print("Funcion bool()")
print()

resultado_bool_1 = bool("mariano")  # retorna True
print(resultado_bool_1)
resultado_bool_2 = bool(None)  # retorna False
print(resultado_bool_2)
resultado_bool_3 = bool(False)  # retorna False
print(resultado_bool_3)
resultado_bool_4 = bool(145)  # retorna True
print(resultado_bool_4)

"""Funcion all()"""

# retorna True si todos los valores son verdaderos
# retorna False si uno de los valores de la lista es False

print("----------------------------------")
print("Funcion all()")
print()

resultado_all_1 = all([12, True, "Mariano"])  # retorna True
resultado_all_2 = all(
    [0, True, "Mariano"]
)  # retorna False porque uno de los datos es False (seria el cero)

print(resultado_all_1)  # retorna True
print(resultado_all_2)  # retorna False

"""Funcion sum()"""
# esta funcion suma todos los valores de un iterable
# tienen que ser numeros porque de lo contrario devuelve un error

print("----------------------------------")
print("Funcion sum()")
print()

# almacenamos en una variable la suma de la lista numeros
suma_total = sum(numeros)
# mostramos en consola la lista numeros
print(f"La suma total de los numeros es {suma_total}")
