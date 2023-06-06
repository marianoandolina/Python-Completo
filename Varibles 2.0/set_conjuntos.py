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







