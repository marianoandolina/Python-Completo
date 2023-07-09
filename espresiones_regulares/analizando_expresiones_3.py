import re

# Vamos a reemplazar todas las vocales por el asterisco

text = "Reemplazando todas las vocales de la cadena por el asterisco"

#   Le indicamos que nos encuentre todas las vocales
# y luego las reemplaze por el asterisco

# con los corchetes le indicamos que busque cada vocal por separado [aeiou]
# si quisieramos que busque todas las vocales juntas literal seria sin corchetes "aeiou" 

new_text = re.sub("[aeiou]", "*", text)

# nos retorna la frase con las vocales reemplazadas
print(new_text)