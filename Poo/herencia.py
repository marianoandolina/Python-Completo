#       HERENCIA SIMPLE 

#       La herencia es clase que hereda metodos y atributos de otra clase

# Creamos la clase
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Hola, estoy hablando un poco")

# Creamos la otra clase que va a heredar de la clase creada anteriormente (Persona)
class Empleado(Persona):
    def __init__(self,nombre, edad, nacionalidad, trabajo, salario):
        # De la siguiente manera le indicamos que es lo que tiene que heredar de la clase padre
        # En este caso va a heredar nombre, edad y nacionalidad de la clase padre
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

    def trabajando(self):
        print("Hola, soy {self.nombre} y estoy trabajando")

# Creamos la instancia de la clase Empleado que es la que hereda de la clase Persona
mariano = Empleado("Mariano","40","Argentino","Aviador",700000)

# Mostramos por pantalla lo que creamos
print(mariano.nacionalidad)
mariano.hablar()
print(f"""
        Nombre = {mariano.nombre} \n
        Edad = {mariano.edad} \n 
        Nacionalidad = {mariano.nacionalidad} \n 
        Trabajo = {mariano.trabajo} \n 
        Salario = {mariano.salario} \n
""")    

#       HERENCIA GERARQUICA 
#
#       Se llama asi cuando hay una clase padre de la cual heredan varias otras, no solo una sola. 






