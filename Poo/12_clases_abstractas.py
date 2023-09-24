from abc import ABC, abstractclassmethod

#       CLASES ABSTRACTAS

#       Una clase abstracta es una clase que no podemos instanciar pero es como una receta.
#       Es una especie de platilla que podemos usar para otras clases, es parecido a herencia pero un poco mas complejo porque la clase abstracta no se puede instanciar como
#       si se puede instanciar una clase padre.
#       De alguna manera estamos haciendo lo mismo que la herencia pero diciendole que ciertas cosas dentro de la clase son obligatorias para crear las demas clases
#       Fomenta el polimorfismo
#       Proporcionan un nivel extra de seguridad


# Creamos la clase abstracta


class Persona(ABC):
    # con este decorador le indicamos que la clase es abstracta
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    # con este decorador le indicamos que el metodo es abstracto
    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(
        self,
    ):  # si no le indicamos nada significa que el metododo es generico
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")


# Al definir un metodo abstracto o un constructor le estamos indicando que al momento de crear la clase que va a heredar la abstraccion tenemos que definir si o si
# estos metodos aunque sea sin ninguna implementacion de codigo para luego poder poder instanciar o de lo contrario dara error.
# Ejemplo de cuando daria error:
"""
# Si nosotros creamos la clase Estudiante que hereda de la clase abstracta Persona tenemos que definirle si o si el metodo hacer_actividad(self)
# de lo contrario si la creamos de la siguiente manera nos tira un error al querer instanciar.

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
"""


# Creamos la clase de manera correcta agregando el metodo hacer_actividad(self)
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")


# Creamos otra clase que tambien hereda de la clase abstracta Persona
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de {self.actividad}")


oriana = Estudiante("oriana", 9, "Masculino", "Primaria 4to grado")
oriana.presentarse()
oriana.hacer_actividad()

mariano = Trabajador("Mariano", 40, "Masculino", "Programador")
mariano.presentarse()
mariano.hacer_actividad()
