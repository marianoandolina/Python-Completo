'''Funciones lambda'''
''' 
Las principales caracteristicas de las funciones lambda son:

---> Son creadas para ahorrar lineas de codigo, para usar menos bloques de memoria
---> Realizan el return de manera automatica
---> No son aptas cuando tenemos que realizar mas de una instruccion
'''


# basicamente es como crear una funcion anonima
# creamos la funcion con el nombre "multiplicar_por_2"
multiplicar_por_2 = lambda x : x*2 

print("-------------------------------------------------")
print("Funciones lambda")
print()
# usando la funcion
# retorna el numero pasado por parametro multiplicado por 2
print(multiplicar_por_2(5)) # muestra por consola 10}

'''
La funcion lambda que vimos arriba:

multiplicar_por_2 = lambda x : x*2 

Es igual a hacer lo siguiente:

def multiplicar_por_2(x):
    return x*2

'''
