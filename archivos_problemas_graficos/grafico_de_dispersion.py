#       UTILIZANDO GRAFICO DE DISPERSION

# importamos las librerias necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# leemos el archivo donde estan los datos
df = pd.read_csv("archivos_problemas_graficos\\dispersion.csv")
# mostramos los datos para chekear que esta leyendo bien el archivo
print(df)

# creamos el grafico de dispersion
# en el eje x va a colocar los datos de la columna llamada "tiempo"
# en el eje y va a colocar los datos de la columna llamada "dinero"
# luego le decimos donde buscar esos datos data=df (variable donde abrimos el csv)
sns.scatterplot(x="tiempo", y="dinero", data=df)

# mostramos el grafico
plt.show()
