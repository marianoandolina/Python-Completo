#       SETTERS Y GETTERS

#   GETTER: Es un concepto para hacer referencia a una funcion que accede a un valor que en teoria tendria que ser privado o muy privado
#   SETTER: Es cuando cambiamos o seteamos ese valor privado o muy privado
class Persona():
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad # cuando tenemos un guion bajo en el atributo le estamos indicando que no acceda al atributo de la forma tradicional, tenemos que crear un getter

def get_nombre(self):
    return self._nombre

dalto = Persona("Lucas","21")
print(dalto._edad) # podemos acceder pero por convencion no es lo correcto, debemos crear un getter

# ESTA ES LA FORMA CORRECTA DE ACCEDER AL ATRIBUTO MUY PRIVADO, A TRAVES DE UN GETTER
class Pepol():
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad # cuando tenemos un guion bajo en el atributo le estamos indicando que no acceda al atributo de la forma tradicional, tenemos que crear un getter

    # creamos el getter para acceder al nombre
    def get_nombre(self):
        return self._nombre

    # este seria el setter y es para cambiar en este caso el atributo _nombre del constructor
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

#       PROBANDO EL GETTER

# creamos el objeto o instancia
marian = Pepol("Mariano","40")

# extraemos el atributo muy privado en la variable
nombre_marian = marian.get_nombre()

# mosrtamos la variable que contiene el atributo muy privado
print(nombre_marian)

# PROBANDO EL SETTER

# cambiamos el nombre con el setter
marian.set_nombre("Pepe")

# lo guardamos a la variable con el getter
nombre_marian = marian.get_nombre()

# mostramos por pantalla el nombre seteado
print(nombre_marian)





