import re

# vamos a detectar un numero de telefono y a ocultarlo

# caden ade texto donde esta el numero
texto = "Hola, pedro, mi numero es: +54 11 4357-4321"

# patron

# encotrar un + literal \+
# al + le siguen 2 numeros \+\d{2}
# encontrar un espacio y luego 2 numeros mas
pattern = r"\+\d{2}\s\d{2}\s\d{4}-\d{4}"

# reemplazo del numero por otra cosa
reemplazo = re.sub(pattern, "(Numero Oculto)", texto)

# mostramos la cadena de texto ya con el reemplazo
print(reemplazo)

