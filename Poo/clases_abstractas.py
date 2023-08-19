from abc import ABC, abstractclassmethod

#       CLASES ABSTRACTAS

#       Una clase abstracta es una clase que no podemos instanciar pero es como una receta.
#       Es una especie de platilla que podemos usar para otras clases, es parecido a herencia pero un poco mas complejo porque la clase abstracta no se puede instanciar como
#       si se puede instanciar una clase padre.

# Creamos la clase abstracta

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")



mariano = Estudiante("Mariano",40,"Masculino","Programacion")
print(mariano.edad)
mariano.hacer_actividad()