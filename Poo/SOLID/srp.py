# SRP

# Ejemplo de clase mal creada porque se encarga nos solo de realizar el movimiento del auto si no tambien del combustible
# Este ejemplo no respeta el primer principio que seria el SRP para que las clases solo realicen una tarea

"""

class Auto:
    def __init__(self):
        self.posicion = 0
        self.combustible = 100

    def mover(self, distancia):
        if self.combustible >= distancia / 2:
            self.posicion += distancia
            self.combustible -= distancia / 2

        else:
            print("No hay suficiente combustible")
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible

"""

# Ejemplo del mismo codigo bien impletmentado respetando el principio SRP

class Auto:
    def __init__(self):
        self.posicion = 0
        self.combustible = 100

    def mover(self, distancia):
        if self.combustible >= distancia / 2:
            self.posicion += distancia
            self.combustible -= distancia / 2

        else:
            print("No hay suficiente combustible")
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible

class Tanque:
    