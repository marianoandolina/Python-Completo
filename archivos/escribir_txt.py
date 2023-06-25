#       ESCRIBIR ARCHIVOS TXT

# abrimos el archivo, le pasamos la ruta
# como primer parametro le indicamos que vamos a sobreescribir en el archivo con la "w"
# y en en el segundo parametro le indicamos como siempre la codificacion
with open("archivos\\texto_prueba.txt", "w", encoding="UTF-8") as archivo:
    # usamos el metodo write() para escribir en el archivo
    archivo.write("Hola, estoy escribiendo en el archivo\n")

    # con writelines() podemos escribir varias lineas
    # le pasamos como parametro una lista con lo que queremos escribir en el archivo
    # las lineas son separadas con \n
    # el metodo writelines() no sobreescribe el archivo si no que va agregando lineas.
    archivo.writelines(["Hola, que onda hermanoo\n", "Rescatate por favor\n"])

    # si aplicamos el mismo metodo otra vez, agrega lineas pero no sobreescribe
    archivo.writelines("Aguante River\n")

    # agregamos otra linea
    archivo.writelines("Otra linea de prueba a ver que onda\n")
