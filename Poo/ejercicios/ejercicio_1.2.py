class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando.")

nombre = input("Digame su nombre: ")
edad = input("Digame su edad: ")
grado = input("Digame su grado: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"El estudiante se llama {estudiante.nombre}, tiene {estudiante.edad} años y cursa en el grado {estudiante.grado}.")

while True:
    estudiar = input()
    if estudiar.lower() == "estudiar":
        estudiante.estudiar()
        break

