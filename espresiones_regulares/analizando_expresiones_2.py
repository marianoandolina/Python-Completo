import re

# cadena en la que se buscaran los patrones

text = "La fecha es 23/6/2023 y el telefono es +1-555-555-5555"

# el patron a buscar
pattern = r"\d{2}/\d{2}/\d{4}"

# el texto con el que reemplazara el patron
replacement = "Fecha oculta"

# reemplazar todas las apariciones del patron en la cadena de texto
new_text = re.sub(pattern, replacement, text)

# mostrar por consola el resultado
print("Texto modificado", new_text)