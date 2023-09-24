"""
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
mostrar(): Muestra los datos de la persona.
esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
"""


class Persona:
    def __init__(self, nombre, apellido, dni):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def dni(self):
        return self.__dni


persona_1 = Persona("Mariano", "Andolina", "30011613")
nombre = persona_1.nombre
apellido = persona_1.apellido
dni = persona_1.dni

print(apellido)
print(nombre)
print(dni)

print(persona_1.nombre)
