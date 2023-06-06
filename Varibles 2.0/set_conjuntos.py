'''CONJUNTOS'''

# creando un conjunto con set
# recordemos que los datos del conjunto no son modificables
# no podemos pasarle al conjunto una lista o diccionario como dato porque tira error
# podemos pasarle una tupla como dato porque tampoco es modificable como los set o conjuntos

print()
print('---------------------------------')
conjunto = set(['dato1','dato2']) # creamos un conjunto o set
print(conjunto, type(conjunto)) # mostramos por consola el conjunto creado

# pasamos una tupla como dato

print('---------------------------------')
conjunto2 = set(['dato1',('tipotupla1','tipotupla2')])
print(conjunto2, type(conjunto2))

# metiendo un conjunto dentro de otro conunto

print('---------------------------------')
conjunto3 = {'datos1','datos2'}

# esto nos tira un error porque no se pueden poner conjuntos dentro de conjunto
# conjunto4 = {conjunto,'dato3'} 
# print(conjunto4)

# para meter un conjunto dentro de otro conunto se hace con la funcion frozenset()
conjunto5 = frozenset(['mandarina1','mandarina2','mandarina3'])
conjunto6 = {conjunto5,'mandarina4'}
print(conjunto6,type(conjunto6))
print('---------------------------------')

'''
TEORIA DE CONJUNTOS

Subconjuntos o superconjuntos
'''

# verificar que un conjunto es un subconjunto de otro
conjunto7 = {1,3,5,7}
conjunto8 = {1,2,7}
resultado = conjunto8.issubset(conjunto7) # usamos issubset() para verificar
print(resultado) 
# Nos retorna False porque el 2 esta en el 7 pero no en el 8
print('---------------------------------')

# probamos de nuevo 

conjunto9 = {1,3,5,7}
conjunto10 = {1,3,7}
resultado2 = conjunto10.issubset(conjunto9) 
print(resultado2) 
# Ahora nos retorna True porque los numeros de conjunto10 estan en el conjunto9
print('---------------------------------')

# otra forma de verificarlo es con el operador de comparacion <= (menor o igual)

conjunto11 = {1,3,5,7}
conjunto12 = {1,3,7}
# esta forma es lo mismo que la forma anterior con issubset()
resultado3 = conjunto12 <= conjunto11 
print(resultado3) 
# nos retorna True igual que la vez anterior
print('---------------------------------')

# verificacion de un superconjunto

conjunto12 = {1,3,5,7}
conjunto13 = {1,3,7}
# en este caso verificamos con el metodo issuperset()
resultado4 = conjunto13.issuperset(conjunto12)  
print(resultado4) 
# nos retorna False porque el conjunto12 es el superset del conjunto13
# la verificacion la pasamos alreves por eso nos devuelve False
# la verificacion correcta seria de la siguiente manera
print('---------------------------------')
resultado5 = conjunto12.issuperset(conjunto13)
print(resultado5) # retorna True
print('---------------------------------')

# y la otra forma de verificar si es un superset es con el operador > (mayor que)

resultado6 = conjunto12 > conjunto13
print(resultado6) # retorna True
print('---------------------------------')

# verificar si hay algun numero en comun

# realiza la verificacion y retorna False tienen 1 elemento en comun
# solamente retorna True cuando los set comparados no tengan ningun elemento en comun
resultado7 = conjunto12.isdisjoint(conjunto13)
print(resultado7) # retorna False
print('---------------------------------')














