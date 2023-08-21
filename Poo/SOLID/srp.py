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


class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible

    def usar_combustible(self, cantidad):
        self.combustible -= cantidad


class Auto:
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("Has movido el auto exitosamente")

        else:
            print("No hay suficiente combustible")

    def obtener_posicion(self):
        print(self.posicion)


tanque = TanqueDeCombustible()
print(tanque.obtener_combustible())
ferrari = Auto(tanque)

ferrari.mover(30)
ferrari.obtener_posicion()
ferrari.mover(50)
ferrari.obtener_posicion()
ferrari.mover(5)
ferrari.obtener_posicion()
ferrari.mover(70)
ferrari.obtener_posicion()
ferrari.mover(50)
ferrari.obtener_posicion()
ferrari.mover(80)
ferrari.obtener_posicion()
