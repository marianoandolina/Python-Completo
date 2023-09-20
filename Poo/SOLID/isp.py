<<<<<<< HEAD
# ISP
# Principio de Segregacion de la interfaz
# Ningun cliente tiene que ser forzado a depender de interface que no utilice
=======
# ISP Interface segregation principle

from django.conf import settings

from abc import ABC, abstractclassmethod

# En el siguiente ejemplo vemos como no se aplica el principio de segregacion de la interface porque en la clase Robot
# tenemos 2 metodos (comer y dormir) que no hacen nada, no sirve de nada que esten alli. 
# Comentamos todo el codigo que esta mal y debajo hacemos el codigo como tendria que ser de la manera correcta

# class Trabajador(ABC):
#     @abstractclassmethod
#     def comer(self):
#         pass

#     @abstractclassmethod
#     def trabajar(self):
#         pass

#     @abstractclassmethod    
#     def dormir(self):
#         pass    

# class Humano(Trabajador):
#     def comer(self):
#         print("El humano esta comiendo")
    
#     def trabajar(self):
#         print("El humano esta trabajando")

#     def dormir(self):
#         print("El humano esta durmiendo")

# class Robot(Trabajador):
#     def comer(self):
#         pass
    
#     def trabajar(self):
#         print("El humano esta trabajando")

#     def dormir(self):
#         pass

class Trabajador(ABC):
    
    @abstractclassmethod
    def trabajar(self):
        pass
class Comedor(ABC):

    @abstractclassmethod
    def comer(self):
        pass
class Durmiente(ABC):

    @abstractclassmethod    
    def dormir(self):
        pass    

class Humano(Trabajador, Durmiente, Comedor):
    def comer(self):
        print("El humano esta comiendo")
    
    def trabajar(self):
        print("El humano esta trabajando")

    def dormir(self):
        print("El humano esta durmiendo")

class Robot(Trabajador):    
    def trabajar(self):
        print("El Robot esta trabajando")

robot = Robot()
humano = Humano()
robot.trabajar()
humano.comer()
humano.dormir()
>>>>>>> 0cf566d6b4b96491a1a3236703d2ee2850649547
