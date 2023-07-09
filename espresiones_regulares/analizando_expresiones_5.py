import re

text = ''' Este es un ejemplo de una pagina web: https://www.example.com y tambien podemos visualizarla'''

#       ANALIZAMOS EL PATRON 

# con el ? le indicamos que si encuentra 1 coincidencia la muestre, si encuentra mas o nada no lo muestre
# si encontras https mostrala https?
# luego del :// literal, y despues la validacion de caracteres del ejercicio 4
# de la a a la z en mayus o minus y el 0-9 el . busca todo menos saltos de linea (el - no se que hace)
# el + le indica que al menos 1 de todo la anterior tiene que estar en este caso uno de lo que esta encerrado entre corchetes https?://[a-zA-Z0-9.-]+
# luego le dice que si o si el patron tiene un punto https?://[a-zA-Z0-9.-]+\.
# el conjunto final despues del punto es un patron ya conocido busca de la a a la z en mayus o minus y el 0-9
# la expresion entre llaves le dice que minimo 2 y maximo nada  https?://[a-zA-Z0-9.-]+\.[a-zA-Z0-9]{2,}

pattern = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z0-9]{2,}"

# le indicamos que busque el patron que le pasamos
result = re.findall(pattern, text)

# mostramos el resultado que encuentra
print(result)

