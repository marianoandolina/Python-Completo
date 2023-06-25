#       WITH OPEN

#       Al leer archivos con with open nos evitamos tener que cerrar el archivo cada vez que lo terminamos de usar

# abrimos el archivo
# por defecto se abre en modo lectura, o sea read o r
# con este comando el archivo se abre y se cierra

with open("archivos\\texto_prueba.txt", encoding="UTF-8"):
    # este print solo se muestra en pantalla si el archivo es abieto
    # es una forma de corroborar que el codigo de la linea 9 funcione correctamente
    print("Leido")

# ahora abrimos el archivo pero lo guardamos en una variable "archivo" usando el operador "as" y le pasamos la codificacion que seria "encoding="UTF-8""
with open("archivos\\texto_prueba.txt", encoding="UTF-8") as archivo:
    # leemos el archivo
    contenido = archivo.read()

    # mostramos su contenido
    print(contenido)

# ** No es necesario cerrarlo al usar "with open()"
 
        