#       METODOS
#       
#       Todas las funciones creadas dentro de la clase se llaman metodos
#       Son acciones que realiza el objeto creado

# Creamos el objeto Celular
class Celular:
    # El metodo __init__ se lo denomina metodo especial, son metodos que python busca en un objeto y ejecuta siempre, nos permite definir muchas cosas.
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    # Creamos el metodo llamar
    # Es muy importante que le pasemos el parametro self para hacer referencia la objeto mismo, de lo contrario da error
    def llamar(self):
        print(f"Estas haciendo una llamada desde un {self.modelo}")
    
    # Creamos el metodo cortar
    # Es muy importante que le pasemos el parametro self para hacer referencia la objeto mismo, de lo contrario da error
    def cortar(self):
        print(f"Estas cortando una llamada desde un {self.modelo}")
    

        
celular_1 = Celular("Samsung","S23","48 MP")
celular_2 = Celular("Apple", "Iphone 15 Pro","96 Mp")

celular_2.llamar()
celular_1.cortar()

    