#       MANEJO DE ARCHIVOS

# usando open para abrir el archivo con una codificacion universal que le pasamos como parametro forzado "encoding="UTF-8" 
archivo_sin_leer = open(r"archivos\texto_prueba.txt",encoding="UTF-8")

# leemos el archivo completo guardado en la variable con el metodo read()
# archivo = archivo_sin_leer.read()

# mostramos lo que hay en el archivo antes abierto y luego leido
# print(archivo)

#       UNA VEZ LEIDO EL ARCHIVO HAY QUE CERRARLO PARA PODER VOLVER A ABRIRLO
#       NOSOTROS EN ESTE CASO LO MANTENEMOS ABIERTO PARA SEGIR MOSTRANDO METODOS

# usando el metodo readlines() nos devuelve una lista con lo que hay en cada linea del archivo
# las lineas estan separadas por \n 
# archivo = archivo_sin_leer.readlines()

# retorna la lista con lo que dice el archivo linea por linea
# print (archivo)

# leer una sola linea con readline()
# si le pasamos un numero por parametro a readline(5) nos lee los primeros 5 caracteres
linea = archivo_sin_leer.readline()

# retorna la primera linea
print(linea)

#       UNA VEZ QUE TERMINAMOS DE USAR EL ARCHIVO TENEMOS QUE CERRARLO CON close()

archivo_sin_leer.close()

# una vez cerrado ya no podemos hacer nada con el archivo
# si queremos volver a utilizarlo devemos usar de nuevo open() para abrirlo
# pero si almacenamos informacion del archivo en variables si las podemos seguir usando
# es importarte cerrarlo poque pueden perderse datos si se cierra de manera inesperada
# tambien es importante porque el mismo archivo limita la cantidad de veces que puede abrirse entonces no lo vamos a poder abrir con otro programa

# **Mucho de este codigo esta comentado para que puedan funcionar las lineas siguientes


















