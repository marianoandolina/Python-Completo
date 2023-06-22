def saludar(name):
    name = name.capitalize()
    return f"Hola {name}, espero que hallas tenido un gran dia"

def compra_o_venta(num):
    if num < 20000:
        print("Compra ya!")
    else: 
        print("No es momento para comprar, espera")

    