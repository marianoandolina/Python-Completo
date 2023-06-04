'''
Se utilizan para ejecutar el codigo si determinada situcion se cumple
'''

'''

Estructura de la condicion

if condicion:
    accion

Si la condicion se cumple pasa a la accion


if True:
    #accion se ejecuta

if False:
    #accion no se ejecuta

'''

edad = 17

# if edad >= 18:
#     print('Podes pasar')
#     print('Forma parte del if')


# Agregamos el else para ejecutar otra accion en el caso de que la condicion sea False

if edad >= 18:  # Condicion (edad es mayor o igual a 18?)
    print('Podes pasar')  # Accion (mostrar el mensaje "Podes pasar")
    print('Forma parte del if')
else:  # Si no se cumple la condicion entra en escena el else
    # Ejecuta esta accion cuando no se cumple la condicion
    print('No podes pasar')
    print('Forma parte del else')

# Comprueba la edad y si la condicion se cumple, pasa a la accion.
# El else tiene que estar identado a la altura del if y lleva :

# Ejemplo basico en un ingreso de usuario

usuario_base_datos = "Mariano Andolina"
usuario_escrito = "Nicolas Rodriguez"

if usuario_base_datos == usuario_escrito:
    print('Ingresando')
else:
    print('No podes ingresar')
