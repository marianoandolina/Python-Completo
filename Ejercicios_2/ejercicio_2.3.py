#       CREANDO UNA FUNCION PARA MOSTRAR LA SERIE DE FIBONACCI DE X NUMERO A X NUMERO

# creamos la funcion
def fibonacci(num):
    # empaquetamos los numeros de inicio de la secuencia en las variables a,b
    a,b = 0,1
    # creamos la lista donde vamos a guardar los numeros fibonacci
    fibonacci_lista = [0]
    # creamos el bucle que cree la secuencia de fibonacci hasta el numero que le pasemos por parametro
    for i in range(num):
        # cuando el numero mas adelantado de la secuencia sea mas grande que el numero pasado por parametro
        # retornamos la lista de los numeros fibonacci y el bucle se termina (como siempre que hay un return)
        if b > num: return fibonacci_lista
        # si no continuamos 
        else:
            # agregamos el ultimo numero a la lista de fibonacci
            fibonacci_lista.append(b) 
            # ahora reemplazamos la secuencia inicial por los numeros actuales
            # es decir que luego del primer bucle la a tiene el valor de b y la b tiene el valor de a+b
            a,b = b,a+b

if __name__ == "__main__":
    # llamamos a la funcion dentro de la variable resultado
    resultado = fibonacci(33)
    # mostramos por consola el resultado
    print(resultado)    
