# CURSO DE POO DE SOY DALTO (https://www.youtube.com/watch?v=HtKqSJX7VoM&t=12s)


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


class Celular():
    marca = "Samsung" # Atributo estatico
    modelo = "S23" # Atributo estatico
    camara = "48mp" # Atributo estatico

# Creamos un objeto a partir de la clase "Celular"
# Este procedimiento se lo conoce como "instanciar un objeto"
# Cuando creamos un objeto estamos creando una instancia de un clase.

celular_1 = Celular()
print(celular_1)

# Para ver la marca del celular y lo mismo para ver modelo y camara
print(celular_1.marca)

# Para cambiar la marca del celular
celular_1.marca = "Motorola"
print(celular_1.marca)

# Esta no es la forma adecuada de trabajar con objetos, pero es la base para comprender clases y sus instancias u objetos.
# Un objeto es una instancia de una clase







