# CURSO DE POO DE SOY DALTO (https://www.youtube.com/watch?v=HtKqSJX7VoM&t=12s)

"""
RECORDATORIO

Camel case = primeraLetraMinuscula (Primmera letra minuscula)
Snake case = separamos_con_guion_bajo
Pascal case = IgualQueCamel (Pero primera letra mayuscula)

Variables = snake_case
Clases y Objetos = PascalCase
"""

#       CLASES
#   
#       Las clases son como las recetas que tenemos que seguir para construir nuestros objetos.
#       Nos permite definir todas las cualidades que va a tener el objeto.
#       
#       OBJETO
#
#       Un objeto es una instancia de una clase.

# Crear una clase
# Por convencion standard para definir una clase se utiliza pascal case
# En esta primera creacion de una clase usamos atributos que son estaticos.

# creamos la clase celular con los atributos estaticos (lo que significa que el objeto que creemos ya va a tener esos atributos.)
class Celular():
    marca = "Samsung" # Atributo estatico
    modelo = "S23" # Atributo estatico
    camara = "48mp" # Atributo estatico

# Creamos un objeto a partir de la clase "Celular"
# Este procedimiento se lo conoce como "instanciar un objeto"
# Cuando creamos un objeto estamos creando una instancia de un clase.
# Al crear un objeto se almacena en la Ram y se elimina al terminar el programa

celular_1 = Celular()
print(celular_1)

# Para ver la marca del celular y lo mismo para ver modelo y camara
print(celular_1.marca) # muestra la marca
print(celular_1.camara) # muestra la camara
print(celular_1.modelo) # muestra el modelo

# Para cambiar la marca del celular
celular_1.marca = "Motorola"
print(celular_1.marca)

# Esta no es la forma adecuada de trabajar con objetos, pero es la base para comprender clases y sus instancias u objetos.
# Un objeto es una instancia de una clase







