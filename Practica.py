area_circulo = lambda radio: 3.14 * radio * radio

print(area_circulo(2))

tu_nombre = lambda nombre: print(f"Hola {nombre}, como estas?")

tu_nombre("Mariano")

colores = ["azul", "verde", "amarillo", "rojo"]

primer_color = lambda color_1: print(
    f"El color que esta en la posicion 1 es el color {color_1[0]}"
)

primer_color(colores)
