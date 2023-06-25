#       CSV

# importamos el modulo csv
import csv

# abrimos el archivo con with open
# al abrir el csv nos lo devuelve como objeto iterable
# entoneces tenemos que recorrerlo con un bucle para ver los datos
with open("archivos\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)

#       Tambien podemos realizar un bucle que agregue la informacion a una variable

# with open("archivos\\datos.csv") as archivo:
#     reader = csv.reader(archivo)
#     datos = []
#     for row in reader:
#         datos.append(row)
#         print(row)
#     print(datos)
