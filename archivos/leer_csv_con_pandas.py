#       PANDAS

#       Pandas es un modulo que nos va a permitir trabajar con csv de manera mas optima

# importamos la libreria pandas como pd
import pandas as pd

# leyendo un archivo csv con pandas
# df hace referencia a "data frame" que es como una especie de archivo de excel
# al no ser un archivo comun tiene distinta forma de comportarse que un archivo
# los data frames contienen filas y columnas
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

# podemos cambiarle el nombre de los enzabezados por parametro
# df = pd.read_csv("archivos\\datos.csv", names=["name", "lastname", "age"])

# mostrando por consola los datos extraidos en la variable archivo
print(df)
print("------------------------------------------")

# mostrando solo la columna "nombre"
print(df["nombre"])

# ahora la columna nombres es name
print(df)
print("------------------------------------------")

# ordenando el data frame por edad, por defecto el orden es ascendente
df_ordenado = df.sort_values("edad")
print(df_ordenado)
print("------------------------------------------")

# ordenandolo de forma descendente
df_ordenado_descendente = df.sort_values("edad", ascending=False)
print(df_ordenado_descendente)
print("------------------------------------------")

# concatenando los dataframes
df_concatenado = pd.concat([df, df2])
print(df_concatenado)
print("------------------------------------------")

# accediendo a las primeras 3 filas con head()
primeras_3_fila = df.head(3)
print(primeras_3_fila)
print("------------------------------------------")

# accediendo a las ultimas 3 filas con tail
ultimas_3_filas = df.tail(3)
print(ultimas_3_filas)
print("------------------------------------------")

# accediendo a la cantidad de filas y columnas con shape
filas_y_columnas_totales = df.shape
print(filas_y_columnas_totales)
print("El primer dato son las filas y el segundo dato son las columnas")
print("------------------------------------------")

# acceder a filas totales
filas_totales = filas_y_columnas_totales[0]
print(filas_totales)
print("------------------------------------------")

# acceder a columnas totales
columnas_totales = filas_y_columnas_totales[1]
print(columnas_totales)
print("------------------------------------------")

# tambien lo podemos hacer desempaquetando
filas_totales_d, columnas_totales_d = df.shape
print(
    f"Las filas totales son {filas_totales_d} y las columnas totales son {columnas_totales_d}"
)
print("------------------------------------------")

# obteniendo data estadistica del dataframe
df_info = df.describe()
print(df_info)
print("------------------------------------------") 

# accediendo a la edad de la fila 2 con loc
elemento_especifico_loc = df.loc[2,"edad"]
print(elemento_especifico_loc)
print("------------------------------------------")

# accediendo a la edad de la fila 2 con iloc
# el primer numero pasado corresponde al numero de fila
# el segundo numero pasado corresponde al indice de la columna 
# los indices de las columnas comienzan en 0 y la primer columna en este caso es "nombre"
elemento_especifico_iloc = df.iloc[2,2]
# nos retorna lo mismo que el anterior, estamos haciendo lo mismo pero buscando solo con indices
print(elemento_especifico_iloc)
print("------------------------------------------")

# accediendo a todas las filas de una columnas
# al no pasarle ningun numero como indice es como si hubieramos puesto 0
# el segundo parametro pasado igual que en el ejemplo anterior es el indice de la columna, en este caso es "apellido"
# recordemos el indice 0 es "nombre", el indice 1 es "apellido" y el indice "2" es edad
# el slicing lo que indica de que fila a que fila vamos a mostrar
apellidos = df.iloc[:,1]
print(apellidos)
print("------------------------------------------")

# mostrando de la fila 0 a la 1
# muestra la fila 0 y la 1
apellidos = df.iloc[:2,1]
print(apellidos)
print("------------------------------------------")

# accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]
print(fila_3)
print("------------------------------------------")

# accediendo a la fila 3 con iloc
fila_3_iloc = df.loc[2,:]
print(fila_3_iloc)
print("------------------------------------------")

# accediendo a filas con edad mayor a 30
mayor_que_30 = df.loc[df["edad"]>30,:]
print(mayor_que_30)
print("------------------------------------------")





