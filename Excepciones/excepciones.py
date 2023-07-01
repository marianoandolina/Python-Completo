#       EXCEPCIONES

#       Las excepciones son errores que aparecen en el codigo y que finalizan el programa
#       Vamos a ver como manejar las excepciones para que nos lance un advertencia pero el programa continue corriendo

# Manejo de excepciones con Try y Except

# creamos una funcion para sumar dos numeros
def sumar_dos():
    # comienzo del bucle para manejar la siguiente excepcion
    while True:
        # pidiendo 2 numeros para sumar    
        a = input("Numero 1: ")
        b = input("Numero 2: ")

        # el try significa "intenta esto"
        try:
            # realiza la suma y la almacena en la variable resultado convirtiendola a entero
            resultado = int(a) + int(b)
            
        # el except significa "si no funciona lo de arriba haz esto"    
        except:
            # si lanza una excepcion en el try se va a ejecutar el except
            print("Te pedi un numero")
            # si el try se ejecuta, no se ejecuta el except, pero si el else
            # si el except se ejecuta, no se ejecuta el else    
        else:
            # el else se ejecuta solamente si se ejecuta el try
            break
        finally:
            print("Finally se ejecuta siempre")
            print("Manejo de excepcion finalizado")

    # retornamos el resultado
    return resultado 
  
sumar = sumar_dos()
print(f"El resultado es {sumar}")


# Otro ejemplo con algunas cosas diferentes
# agregamos al except el objeto Exception que es el padre de todas las excepciones
def sumar_dos_2():
    # comienzo del bucle para manejar la siguiente excepcion
    while True:
        # pidiendo 2 numeros para sumar    
        a = input("Numero 1: ")
        b = input("Numero 2: ")

        # el try significa "intenta esto"
        try:
            # realiza la suma y la almacena en la variable resultado convirtiendola a entero
            resultado = int(a) + int(b)
            
        # el except significa "si no funciona lo de arriba haz esto"    
        # le agregamos Exception as e

        except Exception as e:
            # si lanza una excepcion en el try se va a ejecutar el except
            print("Te pedi un numero")

            # mostramos el error por consola
            print(f"Error: {e}")

            # si el try se ejecuta, no se ejecuta el except, pero si el else
            # si el except se ejecuta, no se ejecuta el else    
        else:
            # el else se ejecuta solamente si se ejecuta el try
            break
        finally:
            print("Finally se ejecuta siempre")
            print("Manejo de excepcion finalizado")

    # retornamos el resultado
    return resultado 
  
sumar_2 = sumar_dos_2()
print(f"El resultado es {sumar_2}")