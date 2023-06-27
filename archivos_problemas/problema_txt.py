#       RESOLUCION DE PROBLEMAS

#       Tenemos 2 listas, una con nombres y otras con apellidos, tenemos que escribir los datos de forma optima con un for

nombres = ["Lucas", "Matias", "Camila", "Pedro", "Roberto"]
apellidos = ["Dalto", "Zing", "Dalto", "Robertix", "Tarado"]

#       Registrar esta informacion en un txt de forma optima

# creamos el archivo y lo abrimos como arch
with open("archivos_problemas_resueltos\\nombres_y_apellidos.txt", "w") as arch:
    # escribimos la primera linea
    arch.writelines("Los datos son:\n\n")

    # realizamos el bucle for para escribir los datos en el archivo txt
    # cuando usamos esta forma de hacer un bucle es importante realizarlo como un array o sea dentro de corchetes
    [
        arch.writelines(f"Nombre: {n}\nApellido: {a}\n------------------\n")
        for n, a in zip(nombres, apellidos)
    ]

#  el bucle de la linea 18 y 19 es lo mismo que hacer lo siguiento

# for n,a in zip(nombres,apellidos):
#     arch.writelines(f"Nombre: {n}\nApellido: {a}\n-------------------\n")

# PARA HACER EL FOR EN UNA SOLA LINEA ES LA SIGUIENTE ESTRUCTURA

# [arch.writelines(f"Nombre: {n}\nApellido: {a}\n------------------\n") for n, a in zip(nombres, apellidos)]
