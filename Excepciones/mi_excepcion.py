
# creando mi propia excepcion
# hereda de la clase Exception
class MiExcepcion(Exception):
    # definimos el constructor que va siempre
    def __init__(self,err):
        print(f"El error es {err}")

# lanzamos la excepcion con raise sin manejarla
## raise MiExcepcion("Te equivocaste, excepcion lanzada")

# lanzando la excepcion manejandola
# ahora con try y except 
try:
    raise MiExcepcion("Te equivocaste, excepcion lanzada")
except:
    print("Como vas a cometer ese error?")
    

    


