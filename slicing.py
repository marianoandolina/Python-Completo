#       SLICING

#       Es una tecnica que nos permite identificar el principio y el final de la forma en la que vamos a acceder a los elementos

# creamos una cadena
cadena = "0123456789"

# mostramos los elementos en la posicion del 4 al 8 (recordamos que la ultima poscion no se incluye)
print(cadena[4:9])

# si no pondemos el primer caracter automaticamente lo toma como un cero
# recorre de la posicion 0 a la 7 (porque la ultima posicion no esta incluida)
print(cadena[:8])

# lo mismo pasa si no ponemos el segundo index
# va a recorrer la cadena desde el 1 hasta el ultimo elemento de la cadena, en este caso el 9
print(cadena[1:])

# si colocamos solo los dos puntos, recorre toda la cadena
print(cadena[:])
