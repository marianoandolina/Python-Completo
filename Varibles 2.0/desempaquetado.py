'''DESEMPAQUETADO DE VARIABLES'''

'''LO QUE HACE EL EMPAQUETADO Y DESEMPAQUETADO ES CREAR UNA LISTA,
TUPLA ETC, Y LUEGO ASIGNARLE VARIABLES A CADA ELEMTO DE ESA TUPLA
O LISTA O LO QUE SEA'''

# creamos una tupla dentro de la variable datos
datos_en_tupla = ('mariano', 'andolina')  # tupla
datos_en_lista = ['castanio', 'corto']  # lista

# asignamos esos datos a 2 nuevas varibles llamadas nombre y apellido
# cabe destacar que tenemos que crear la misma cantidad de variables como cantidad de datos tenga el array

# desempaquetado
# tenemos 2 variables (nombre, apellido) y 2 datos en la variable datos (mariano, andolina)
# no se pueden desempaquetar numeros

nombre, apellido = datos_en_tupla  # desempaquetado
color_pelo, tipo_pelo = datos_en_lista  # desempaquetado

print('--------------------')
print(nombre)  # muestra la nueva variable
print(apellido)  # muestra la nueva variable
print('--------------------')
print(color_pelo)  # muestra la nueva variable
print(tipo_pelo)  # muestra la nueva variable
print('--------------------')

# Tambien podemos agregar un tercer dato

# agregamos la edad dentro de datos
datos_en_tupla = ('mariano', 'andolina', 40)

# asignamos el nuevo dato
nombre, apellido, edad = datos_en_tupla

print()
# muestra el nuevo dato que agregamos
print(edad)
