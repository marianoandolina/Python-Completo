#       TRABAJANDO CON PAQUETES

#       Un paquete es un conjunto de modulos que vamos a importar para poder trabajar en nuestro proyecto

# creamos una carpeta llamada paquete que va a contener varios modulos
# ahora de esa carpeta importamos el modulo saludar que contiene la funcion saludar
import paquete.saludar

# ejecutamos y mostramos por pantalla la funcion saludar dentro del paquete llamado paquete y el modulo llamado saludar.
print(paquete.saludar.saludar("Mariano"))

print(paquete.__path__)
