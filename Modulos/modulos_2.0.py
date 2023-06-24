#       ENRUTAMIENTO DE MODULOS

#       Cuando tenemos que importar modulos que se encuentren en una carpeta diferente se hace de la siguiente manera

# para importar directamente todo sin from
import funciones_buenas.saludar as m_saludin


# importamos modulo_saludar_2 que se encuentra en la carpeta funciones_buenas
# from funciones_buenas import saludar

# utilizamos la funcion saludar dentro del modulo llamado modulo_saludar_2 de la carpeta funciones_buenas
saludo = m_saludin.saludar("Mariano")

# mostramos por consola
print(saludo)
print(m_saludin.__name__)

#       COMO ACCEDER CUANDO LA CARPETA NO ESTA EN LA MISMA RUTA

#       En este caso la carpeta esta afuera de donde estamos ubicados con el modulo actual

# cuando la carpeta no se encuentra en la misma ruta
# tenemos que importar sys que es un modulo de python

import sys

print(sys)  # muestra que es sys
print(sys.builtin_module_names)  # muestra todos los modulos que estan dentro de sys
print(
    sys.path
)  # muestra la ruta actual donde estamos ubicados y todas las rutas donde hay modulos instalados

# agregamos al path la carpeta donde se encuentra el modulo que debemos o queremos importar
# esto no queda de manera permanente, es por sesion, para instalarlo de manera permanente se hace de una manera diferente

sys.path.append(
    "C:\\Users\\maria\\OneDrive\\Escritorio\\Programacion\\Python\\Resumen\\ejemplo_enrutamiento"
)

print(sys.path)

# aunque lo marque como error esta funcionando
import saludar_afuera as mod_sal

# utilizamos el modulo que agregamos al path
print(mod_sal.saludar("Mariano"))
