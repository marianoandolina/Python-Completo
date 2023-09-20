class Perro:
    def __init__(self, nombre, color, raza, sexo):
        self.nombre = nombre.capitalize()
        self.color = color.capitalize()
        self.raza = raza.capitalize()
        self.sexo = sexo.capitalize()
    
    def ladrar(self):
        return f"{self.nombre} de raza {self.raza} esta ladrando"
    
    def comer(self):
        return f"{self.nombre} de raza {self.raza} esta comiendo"

    def correr(self):
        return f"{self.nombre} de raza {self.raza} esta corriendo"

    def __str__(self):
        celular = f"Perro {self.raza} con el nombre de {self.nombre} de color {self.color}"
        return celular


perro_1 = Perro("MARLON","marron", "boxer", "macho")
print(perro_1.nombre)

perro_2 = Perro("gina","chocolate","labrador","hembra")
print(perro_2.nombre)

print(perro_1.ladrar())
print(perro_1.comer())
print(perro_1.correr())

print(perro_2.ladrar())
print(perro_2.comer())
print(perro_2.correr())




