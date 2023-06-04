''' 
El condicional elif (else if) que seria "si no" "si no se cumple tal condicion, fijate esta otra"
'''

# Definimos una variable con un valor
ingreso_mensual = 11000

if ingreso_mensual > 10000: # Hacemos el condicinal, si la variable ingreso_mensual cumple la condicion pasa a la accion
    print('Estas bien en cualquier parte del mundo') # Accion

elif ingreso_mensual > 1000: # Si no se cumple la primera condicion pasa realizar la comprobacion de esta otra condicion
    print('Estas bien en latinoamerica') # Accion

else: # Con el else lo que hacemos es decirle que si ninguna de las condiciones anteriores se cumplen, realiza la siguiente accion
    print('Sos pobre') # Accion

# Se pueden poner muchos elif

if ingreso_mensual > 10000: # Hacemos el condicinal, si la variable ingreso_mensual cumple la condicion pasa a la accion
    print('Estas bien en cualquier parte del mundo') # Accion

elif ingreso_mensual > 500: # Hacemos el condicinal, si la variable ingreso_mensual cumple la condicion pasa a la accion
    print('Estas bien en Argentina') # Accion

elif ingreso_mensual > 1000: # Si no se cumple la primera condicion pasa realizar la comprobacion de esta otra condicion
    print('Estas bien en latinoamerica') # Accion

elif ingreso_mensual < 50: # Hacemos el condicinal, si la variable ingreso_mensual cumple la condicion pasa a la accion
    print('Estas en la indigencia') # Accion 

else: # Con el else lo que hacemos es decirle que si ninguna de las condiciones anteriores se cumplen, realiza la siguiente accion
    print('Sos pobre') # Accion

# if anidados o varias condiciones

gasto_mensual = 3000

if ingreso_mensual > 10500:
    if ingreso_mensual - gasto_mensual < 0:
        print('Estas en deficit')
    elif ingreso_mensual - gasto_mensual > 3000:
        print('Estas bien')    
    else:
        print('Estas gastando mucho, hay que ver si te alcanza')



 
    



