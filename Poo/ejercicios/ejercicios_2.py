#       EJERCICIO 2
#       Ejercicio de herencia y uso de super


"""
Crear un sistema para una escuela. En este sistema vamos a tener 2 clases principales: Persona y Estudiante. 
La clase Persona tendra los atributos nombre y edad y un metodo que imprima el nombre y la edad de la persona.
La clase Estudiante heredara de la clase Persona y tambien tendra un atributo adicional, grado y un metodo que 
imprima el grado del estudiante.

Deberas realizar super() en el metodo de iniciacion __init__ para reutilizar el codigo de la clase padre (Persona).
Luego crea una instancia de la clase Estudiante e imprime sus atributos, y utiliza sus metodos para asegurarte que
todo funcione correctamente.
"""



class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre} \nEdad: {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_grado(self):
        print(f"Grado: {self.grado}")

persona_1 = Estudiante("Oriana",9,4)
print(persona_1.nombre)
print(persona_1.edad)
print(persona_1.grado)

persona_1.mostrar_datos()
persona_1.mostrar_grado()



