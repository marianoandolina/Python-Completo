#       ENCAPSULAMIENTO

#       No existe como tal en Python
#       Es una manera de proteger la informacion o lo que no queremos que vea el desarrollador

# atributos privados
class MiClase:
    def __init__(self):
        # creamos un atributo privado, la forma de crearlo es colocando el _ luego del self. ej: self._atributo_privado
        self._atributo_privado = "valor"

objeto = MiClase()
print(objeto._atributo_privado)

# atributos muy, muy privados es cuando utilizamos doble guion bajo __

class MiClase2:
    def __init__(self):
        # creamos un atributo privado, la forma de crearlo es colocando el doble __ luego del self. ej: self.__atributo_muy_privado
        self.__atributo_muy_privado = "valor"
    
    def __hablar(self):
        print("Estoy hablando")

objeto2 = MiClase2()
# print(objeto2.__atributo_muy_privado) # esto nos devuelve un error porque el atributo esta realmente oculto y no lo puede mostrar
print(objeto2.__hablar()) # tambien nos tira un error porque el metodo es muy privado y no es accesible de esta manera

# para acceder y modificar los tipos de atributos privados y muy privados usamos getters y setters (ver archivo especifico)





