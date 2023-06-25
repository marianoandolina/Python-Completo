#       AGREGANDO AL ARCHIVO TXT CON APPEND

#       LA DIFERENCIA DEL APPEND CON EL WRITE ES QUE EL WRITE SOBREESCRIBE TODO EL TIEMPO PERO
#       EL APPEND VA AGREGANDO EN CADA EJECUCION

# abrimos el archivo, le pasamos la ruta
# como primer parametro le indicamos que vamos a agregar en el archivo con la "a" (* la "a" es de append)
# y en en el segundo parametro le indicamos como siempre la codificacion
with open("archivos\\texto_prueba.txt", "a", encoding="UTF-8") as archivo:
    # usamos el metodo write() para escribir en el archivo
    archivo.write("Hola, estoy escribiendo en el archivo\n")
    # usando un bucle para agregar varias lineas
    for i in range(5):
        archivo.write(
            f"Linea {i+1} agregada\n"
        )  # es i+1 porque de lo contrario  empezaria desde el 0
