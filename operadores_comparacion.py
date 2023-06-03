'''
Los operadores de comparacion son los siguientes

==  Igual que
!=  Distinto de
<   Menor que
<=  Menor o igual que 
>   Mayor que 
>=  Mayor o igual que

'''

# Los operadores de comparacion nos devuelven True o False

igual_que = 5 == 6  # Devuelve False

distinto_de = 5 != 6  # Devuelve True

mayor_que = 5 > 6  # Devuelve False

menor_que = 5 < 6  # Devuelve True

mayor_o_igual_que = 5 >= 6  # Devuelve False

menor_o_igual_que = 5 <= 6  # Devuelve True

print(igual_que)
print(distinto_de)
print(mayor_que)
print(menor_que)
print(mayor_o_igual_que)
print(menor_o_igual_que)
print()

# Calculos combinados

a = 5
b = 10
c = 20

comparacion = a + b > c  # Devuelve False
print(comparacion)
print()

# Ejemplo de usuario para ingresar a un sitio

usuario_base_datos = "Mariano Andolina"
usuario_escrito = "Nicolas Rodriguez"

print(usuario_base_datos == usuario_escrito)  # Devuelve False

usu_reg = "Mariano Andolina"
usu_ing = "Mariano Andolina"

print(usu_reg == usu_ing)  # Devuelve True
