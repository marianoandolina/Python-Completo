import re 

text = "The quick brown fox jumps over the lazy dog"

#       La busqueda dice lo siguiente

# buscame una cadena donde The aparezca al principio (^The)
# encontra cualquier cosa que no sea un espacio en linea (.)
'''el asterisco afecta al anterior operador, en este caso el punto'''
# lo que el astrisco le dice al punto es que encuentr 0 o mas, si encuentra 0 no pasa nada y si encuentra mas las retorna
# buecame el la cadena la palabra dog al final de la linea

x = re.search("^The.*dog$", text)

if x:
    print("si")
else:
    print("no")

