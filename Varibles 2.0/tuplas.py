'''VAMOS A ADENTRARNOS UN POCO MAS EN LO QUE SON LAS TUPLAS'''

'''
Cuando debemos crear tuplas ?

Cuando los datos sean de solo lectura ya que son mas eficientes porque ocupan
menos memoria que las listas.

Las listas las usamos para datos mas flexibles. Datos que modificaremos de manera mas frecuentes
'''

# creamos una tupla con tuple()
# nombramos la tupla y le tenemos que pasar una lista como parametro a la funcion tuple

tupla1 = tuple(['dato_1', 'dato_2'])

# tambien se pueden crear tuplas de la siguiente manera
# creamos las tuplas sin parentesis
tupla2 = 'dato_1', 'dato_2'

# cuando queremos crear una tupla con un solo dato le ponemos la coma al final
tupla3 = 'dato_1',

# mostramos que todas las tuplas se crearon igual usando 3 maneras diferentes
print('----------------------')
print(tupla1, type(tupla1))
print(tupla2, type(tupla2))
print(tupla3, type(tupla3))
print('----------------------')
