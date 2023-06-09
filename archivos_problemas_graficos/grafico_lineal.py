#       UTILIZANDO GRAFICO DE LINEAS

# importamos las librerias necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# leemos el archivo donde estan los datos
df = pd.read_csv("archivos_problemas_graficos\\pedos.csv")
# mostramos los datos para chekear que esta leyendo bien el archivo
print(df)

# creamos el grafico
# en el eje x va a colocar los datos de la columna llamada "fecha"
# en el eje y va a colocar los datos de la columna llamada "pedos"
# luego le decimos donde buscar esos datos data=df (variable donde abrimos el csv)
sns.lineplot(x="fecha", y="pedos", data=df)

# en el punto 01-09 del eje x y el 17 del eje y colocamos una o un circulo
plt.plot("01- 09", 17, "o")

# mostramos el grafico
plt.show()
