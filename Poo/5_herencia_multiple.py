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
    # en este caso que estamos usando metodos, si usamos self nos trae el metodo de la clase actual y si usamos super() nos trae el metodo de la clase padre.
    def presentarse_clase_padre(self):
        return f"Hola, soy {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.empresa}"
    
    # creamos este metodo para probar los diferentes tipos de mostrar el metodo padre y el metodo de la clase en la que estamos
    def mostrar_habilidad(self):
        return "No tengo habilidad ninguna, ajjajajaja"

    # tenemos creado el metodo mostrar_habilidad en la clase Artista y tambien en la clase EmpleadoArtista 
    # self:  nos muestra el metodo que tenemos creado en esta clase
    # super():  nos muestra el metodo que tenemos creado en la clase padre
    # creamos el metodo presentarse pero ahora mostrando el metodo mostrar_habilidad de esta clase y no de la clase padre

    def presentarse(self):
        return f"Hola, soy {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}"
    

# creamos a la presona con toda la informacion
persona_1 = EmpleadoArtista("Mariano","40","Argentina","Guitarrista","200000","Sony")
print(persona_1.nombre)

# mostramos los llamados a metodos del mismo nombre pero de diferentes clases

print(persona_1.presentarse_clase_padre())
print(persona_1.presentarse())


# issubclass(param1, param2)

# Para saber si una clase heredad de otra usamos issubclass()
herencia = issubclass(EmpleadoArtista, Persona)
# mostramos por pantalla, True or False
print(herencia) # nos muestra True porque EmleadoArtista hereda de Persona
# chequeamos ahora si Artista es subclase de Persona, nos tiene que devolver False porque no lo es
herencia_2 = issubclass(Artista, Persona)
print(herencia_2)

# isinstance(param1, param2)

# Usamos isinstance() para saber si un objeto o instancia pertenece a una clase

instancia = isinstance(persona_1,EmpleadoArtista) # 
print(instancia) # Nos devuelve True

# en el caso de que la clase herede de otra tambien nos va a dar True

instancia_2 = isinstance(persona_1, Artista)
print(instancia_2) # devuelve True

instancia_3 = isinstance(persona_1, Persona)
print(instancia_3) # devuelve True






