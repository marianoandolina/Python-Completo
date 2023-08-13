#       METHOD RESOLUTION ORDER (mro)

#       Define el orden por el cual python llama atributos y metodos en las clases

class A:
    def hablar(self):
        print("Hola desde clase A")       

class B(A):
    def hablar(self):
        print("Hola desde clase B")      

class C(A):
    def hablar(self):
        print("Hola desde clase C")      

class D(B,C):
    def hablar(self):
        print("Hola desde clase D")      

d = D()
d.hablar()
