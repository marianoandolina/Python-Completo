'''Input es para pedirle al usuario que ingrese datos'''

# Los datos que ingresamos siempre los guarda en str salvo que nosotros indiquemos lo contrario

# Podemos ingresar str o numeros pero siempre se guardan como str o sea como texto
nombre = input('Ingresa tu nombre: ')
print(f'El nombre es {nombre}')

# Para ingresar un numero se hace de la siguiente manera

print()
# Funciona solamente ingresando numeros, si ingresamos un str nos da error
# Solo podemos ingresar numeros int, si ingresamos float nos da error
numero_int = int(input('Ingresa un numero: '))
resultado = numero_int * 2
print(resultado)

# Para ingresar un numero float
print()
# Podemos ingresar cualquier numero (float o int)
numero_float = float(input('Ingresa un numero: '))
print(numero_float)  # Muestra el numero con decimales
