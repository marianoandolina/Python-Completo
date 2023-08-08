# CURSO DE POO DE SOY DALTO (https://www.youtube.com/watch?v=HtKqSJX7VoM&t=12s)

#       ATRIBUTOS
#       
#       Los atributos son caracteristicas de la clase que creamos
#       Los atributos se crean a cuando instanciamos una clase (cuando creamos un objeto)
#

# Cremos una clase que nos premita cargarle los atributos al instanciar el objeto
# Para esto tenemos que crearla con la siguiente estructura

class Celular:
    # La siguiente funcion es una funcion que se ejecuta automaticamente siempre cuando creamos un objeto.
    # La funcion es un constructor def __init__
    
    def __init__(self, marca, modelo, camara):
        self.marca = marca # El primer marca no es igual que el segundo, el segundo marca accede al parametro del constructor __init__
        self.modelo = modelo
        self.camara = camara

# self : El self hace referencia al mismo objeto, por ejemplo decir self.marca es como decir celular.marca

# Instanciamos el objeto celular_1
# Al crearlo colocamos los parametros que definimos en el constructor pero sin el self
# El self no se pasa nunca en los parametros 

celular_1 = Celular("Samsung", "S23", "48mp")
print(celular_1.marca)

# Creamos otro celular
celular_2 = Celular("Apple","Iphone 15 pro","96MP")
print(celular_2.marca)




