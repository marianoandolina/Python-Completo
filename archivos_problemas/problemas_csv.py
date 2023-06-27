#       CAMBIAR EL TIPO DE DATO DE UNA COLUMNA

# importamos pandas
import pandas as pd

# leemos el contenido del archivo
df = pd.read_csv("archivos_problemas\\datos.csv")

# cambiamos los tipos de datos que ahora van a ser strings
df["edad"] = df["edad"].astype(str)

# verificamos que tipo de datos son los que estan en la columna edad
# verificamos que tipo de dato es el que esta en la columna edad en el index 0
print(type(df["edad"][0])) # retorna <class 'str'>

# reemplazar valores "dalto" por "maestro"
# le indicamos que de la columna apellido, cambie usando el metodo .replace() 
# el primer parametro de replace es el dato a reemplazar, el segundo es por cual reemplazarlo y el tercero es inplace=True

df['apellido'].replace('dalto', 'maestro', inplace=True)
print(df['apellido'])

# eliminando las filas repetidas
# primero mastramos los datos 
print(df)

# eliminamos las filas con datos incompletos
df = df.dropna()

# volvemos a motrar todos los datos
print(df)

# eliminando filas repetidas
df = df.drop_duplicates()
print(df)

# creando un dataframe con todas las modificaciones que le hicimos (limpio)
df.to_csv("archivos_problemas\\datos_modificados.csv")










