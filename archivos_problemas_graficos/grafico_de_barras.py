#       UTILIZANDO GRAFICO DE BARRAS

# importamos las librerias necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# leemos el archivo donde estan los datos
df = pd.read_csv("archivos_problemas_graficos\\cofla_ingresos.csv")
# mostramos los datos para chekear que esta leyendo bien el archivo
print(df)

# creamos el grafico de barras
# en el eje x va a colocar los datos de la columna llamada "fecha"
# en el eje y va a colocar los datos de la columna llamada "pedos"
# luego le decimos donde buscar esos datos data=df (variable donde abrimos el csv)
sns.barplot(x="fuente", y="ingresos", data=df)

# colocamos un titulo al grafico
plt.title("Ingresos de cofla")

# sumamos el total de ingresos para mostrar en un grafico
total_ingresos = df["ingresos"].sum()

# mostramos el total por consola
print(f"El total de ingresos de Cofla es US$ {total_ingresos}")

# mostramos el grafico
plt.show()
