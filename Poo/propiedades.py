#       LAS PROPIEDADES

#       Nos permiten definir getters, setters y deletters tambien


class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property  # este es un decorador reservado para las clases que le indica que la funcion que sigue es un getter
    # de esta manera al llamar a la funcion no hace falta que agreguemos los parentesis
    # ademas hace que la propiedad sea mas dificil de modificar, no modificable a traves de las maneras tradicionales
    def nombre(self):
        return self.__nombre

    # para poder modificar valores tenemos que crear el setter
    @nombre.setter  # este decorador tiene el nombre de la propiedad que queremos modificar seguido del .setter
    def nombre(self, new_name):
        self.__nombre = new_name

    # para poder borrar una propiedad usamos un deleter
    @nombre.deleter
    def nombre(self):
        del self.__nombre


mariano = Persona("Mariano", "40")
nombre = mariano.nombre
print(nombre)

# formas tradicionales para modificar que en este caso no podemos usar
# dalto.__nombre = "Joselito"

# forma correcta de modificar la propiedad mediante el setter creado en la clase con decorador

mariano.nombre = "Pepe"
nombre = mariano.nombre
print(nombre)

# para borrar simplemente usamos el deleter

del mariano.nombre

print(nombre)

# en este caso no funciono, a Dalto le funciono y tiene el codigo igual pero aca no me elimina el nombre.

# el uso de esta sintaxis de getters, setters y deleters tiene ventaja sobre la otra forma de usarlos que vimos en encapsulamientos.
