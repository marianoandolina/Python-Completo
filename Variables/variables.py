# Las variables almacenan informacion que sea util.

a = 15  # Declaramos la variable y la definimos.
# Las variables son variables justamente porque pueden cambiar. En esta linea redefinimos la varible que esta declarada.
a = 10  # Ahora la variable vale 10.
a = "Mariano"  # Ahora la variable tiene el str "Mariano"

# Tambien podemos hacer sumas de numeros y strings en variables.

b = 1
c = 2
d = b + c

# Muestra en la consola el valor de la varible d que es la suma de b + c.
print(d)  # Muestra 3

# Sumar numeros en varibles.
numero = 10
# Le podemos sumar 1 de esta manera
numero = 10 + 1
# Y tambien le podemos sumar un numero de la siguiente manera
# El + adelante del igual significa que a esa variable le sumamos el numero que anotemos despues del = .
numero += 1
# Lo mismo podemos hacer para restar
numero -= 1  # A la variable "numero" le resta el numero que le indiquemos.

# CONCATENACION #
# Concatenar es unir
nombre = 'Mariano'
# En este caso unimos una variable que contiene un string con 2 strings.
print('Hola ' + nombre + ' Como estas?')

# f STRINGS
# Usamos la f delante u luego las {} para llamar una variable dentro de las comillas.

apellido = 'Andolina'
print(f'Hola {nombre} {apellido}, como estas?')

# Tambien podemos usar el f dentro de una variable.

nombre_completo = f'Mi nombre completo es {nombre} {apellido}'
print(nombre_completo)

# Para borrar una variable definida podemos usar el operador "del".

del nombre_completo  # Borramos la variable.
# Al ejecutar nos tira el error que la variable no esta declarada.
print(nombre_completo)
