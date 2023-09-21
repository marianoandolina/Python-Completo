class Motocicleta:
    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.motor = False
    
    def arrancar(self):
        if self.motor == False:
            self.motor = True
            print(f"La moto matricula {self.matricula} arranco")
        elif self.motor == True:
            print(f"La moto matricula {self.matricula} ya esta en marcha")
    
    def detener(self):
        if self.motor == True:
            self.motor = False
            print(f"La moto {self.matricula} se detuvo")
        elif self.motor == False:
            print(f"El motor de la moto matricula {self.matricula} ya se encuentra detenido.")


moto_1 = Motocicleta("negra", "HIR749", 10, 2, "Yamaha", "ybr125", "20 - 9 - 2023", "110 km", "140 kg")

print(moto_1.modelo)
moto_1.arrancar()
print(moto_1.motor)
moto_1.arrancar()
moto_1.detener()
moto_1.detener()
print(moto_1.motor)
