"""
Bucle while o while loop

Es una sentencia que nos permite ejecutar un codigo bastantes veces, 
la diferencia con el for radica en que el for recorre elementos mientras
que el while se va a ejecutar siempre que se cumpla una condicion pactada
"""
print()
print("-------------------------------")

# establecemos una variable contador que va a acumular un numero
contador = 0

# mientras el contador sea menor a 10 se ejecuta el bucle
while contador < 10:
    # muestra por consola el numero almacenado en el contador
    print(contador)
    # agrega 1 a la variable contador y ahora vale 1
    contador += 1

print(f"El bucle llego a su fin porque contador vale {contador}")
