#       HERENCIA MULTIPLE

#       Es cuando creamos una clase y tiene varias herencias. 

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Hola, estoy hablando un poco")

# Creamos la otra clase que va a heredar de la clase creada anteriormente (Persona)
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"

# creamos la clase que va a heredar de multiples clases (Persona, Artista)
# en vez de llevar el sub constructor que comienza con super(), reemplazamos el super() por cada clase de la que vamos a heredar y entre parentesis los atributos que vamos a heredar.
class EmpleadoArtista(Persona, Artista):
    # constructor
    def __init__(self,nombre, edad, nacionalidad,habilidad,salario,empresa):
        # subconstructores con las herencias de cada clase
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)

        self.salario = salario
        self.empresa = empresa

    # para heredar un metodo de la clase padre utilizamos super()
    def presentarse(self):
        return f"Hola, soy {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.empresa}"

# creamos a la presona con toda la informacion
persona_1 = EmpleadoArtista("Mariano","40","Argentina","Guitarrista","200000","Sony")
print(persona_1.nombre)
print(persona_1.presentarse())

