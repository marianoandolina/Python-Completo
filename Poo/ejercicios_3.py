#       EJERCICIOS 3

"""
        CREAR JUEGO FUSION

    El juego consiste en crear personajes de un juego y  que estos personajes se puedan fusionar
    para formar personajes mas poderosos que tengan mas poder...

    Para ello debemos cambiar el comportamiento del operador + para que cuando los personajes se
    fusionen salga un nuevo personaje con habilidades mejoradas.

    Una posible formula es: 
        El promedio de las habilidades de ambos al cuadrado
"""

# Implementacion del codigo del juego Fusion

class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza 
        self.velocidad = velocidad 
    
    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
    
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**1.34)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**1.34)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

goku = Personaje("Goku", 100, 100)
vegueta = Personaje("Vegueta", 99, 99)
jiren = Personaje("Jiren", 130, 140)

gogueta = goku + vegueta
jireta = gogueta + jiren

print(goku)
print(vegueta)
print(jiren)
print(gogueta)
print(jireta)




