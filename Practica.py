nombre = "Mariano"
apellido = "Andolina"
edad = '40'

datos_mariano = list[apellido, nombre, edad]

print(datos_mariano)

datos_mariano2 = dict(nombre=nombre, apellido=apellido, eda=edad)
print(datos_mariano2)

datos_mariano_3 = dict().fromkeys(
    ['nombre', 'apellido', 'edad'], [nombre, apellido, edad])
print(datos_mariano_3)
