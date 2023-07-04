#       EXPRESIONES REGULARES

#       Primero comenzamos con ejemplos de busquedas simples.

import re

texto = """Hola. Como estas, esta es la cadena 1.?
Esta es la segunda linea de texto o sea 2.
Y esta es la tercera linea de texto, entonces por supuesto seria la 3 o tres.
"""
print("-----------------------------------------------------------------")

# busca la palabra hola y guarda el resultado en la variable resultado
resultado = re.search("Hola", texto)

# mostramos el resultado por consola
print(resultado)
print("-----------------------------------------------------------------")

resultado_2 = re.findall("esta", texto)
print(resultado_2)
print("-----------------------------------------------------------------")
# podemos usar flags para ser mas especificos

# por ejemplo en esta linea de comandos le agregamos flags=IGNORECASE
# lo que hace IGNORECASE es ignorar mayusculas o minusculas y retornar todas las coincidencias
resultado_3 = re.findall("esta", texto, flags=re.IGNORECASE)
print(resultado_3)
print("-----------------------------------------------------------------")

#       EJEMPLOS DE EXPRESIONES REGULARES

# \d --> busca digitos numericos del 0 al 9

resultado_4 = re.findall(r"\d", texto)
print(resultado_4)
print("-----------------------------------------------------------------")

# \D --> busca todo lo que no sean digitos numericos del 0 al 9
# al poner mayuscula invierte la busqueda casi siempre

resultado_5 = re.findall(r"\D", texto)
print(resultado_5)
print("-----------------------------------------------------------------")

# \w --> busca todo lo que sean caracteres alfanumericos [a-z,A-Z,0-9, _]

resultado_6 = re.findall(r"\w", texto)
print(resultado_6)
print("-----------------------------------------------------------------")

# \W --> busca todo lo que NO SEAN caracteres alfanumericos

resultado_7 = re.findall(r"\W", texto)
print(resultado_7)
print("-----------------------------------------------------------------")

# \s --> busca espacios en blanco y saltos de lineas

resultado_8 = re.findall(r"\s", texto)
print(resultado_8)
print("-----------------------------------------------------------------")

# \S --> busca todo menos espacios en blanco y saltos de linea

resultado_9 = re.findall(r"\S", texto)
print(resultado_9)
print("-----------------------------------------------------------------")

# . --> busca TODO MENOS saltos de linea

resultado_10 = re.findall(r".", texto)
print(resultado_10)
print("-----------------------------------------------------------------")

# \n --> busca TODO lo que sean saltod de linea

resultado_10 = re.findall(r"\n", texto)
print(resultado_10)
print("-----------------------------------------------------------------")

# \n --> cancela caracteres especiales

# cancelando la busqueda de todo y buscar puntos.
resultado_11 = re.findall(r"\.", texto)
print(resultado_11)
print("-----------------------------------------------------------------")

# armar una cadena que busque un numero, seguido de un punto y un espacio

resultado_12 = re.findall(r"\d\.\s", texto)
print(resultado_12)
print("-----------------------------------------------------------------")
