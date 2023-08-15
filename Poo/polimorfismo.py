#       POLIMORFISMO

#       Es darle una orden a un objeto y obtener diferentes respuestas de acuerdo a sus atributos

class Gato():
    def sonido(self):
        return "Miau"

class Perro():
    def sonido(self):
        return "Guau"

def hacer_sonido(animal):
    print(animal.sonido())

gato = Gato()
perro = Perro()

# POLIMORFISMO DE FUNCION

# le pasamos la misma funcion en este caso sonido() y nos devuelve cosas diferentes
print(gato.sonido()) 
print(perro.sonido())

# en este caso la funcion es la misma y lo que cambia es el parametro que le pasamos
hacer_sonido(gato)
hacer_sonido(perro)

# POLIMORFISMO DE HERENCIA O CON HERENCIA, TAMBIEN LLAMADO DE SUBCLASE

