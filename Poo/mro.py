#       METHOD RESOLUTION ORDER (mro)

#       Define el orden por el cual python busca atributos y metodos en las clases

class A:
    def hablar(self):
        print("Hola desde clase A")       

class B(A):
    def hablar(self):
        print("Hola desde clase B")      

class C():
    def hablar(self):
        print("Hola desde clase C")      

class D(C):
    def hablar(self):
        print("Hola desde clase D")      

d = D()
d.hablar()

# practicar mro
# para saber el orden de ejecucion podemos usar el metodo mro()

# ej:

print(D.mro())

