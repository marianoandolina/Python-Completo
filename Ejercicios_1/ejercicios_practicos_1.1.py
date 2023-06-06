# Para resolver el ejercicio, lo primero que tenemos que hacer es anotar los datos

# a)

# Duracion de cursos
este_curso = float(1.5)
curso_minimo = float(2.5)
curso_promedio = float(4)
curso_maximo = float(7)

# Diferencia de duracion
diff_rapido = 100 - este_curso / curso_minimo * 100
diff_lento = 100 - este_curso / curso_maximo * 100
diff_promedio = 100 - este_curso / curso_promedio * 100

print('--------------------')
print('El curso de Dalto dura:')
print(
    f'- Un {diff_rapido:.2f} % menos que el curso mas rapido'
)
print(
    f'- Un {diff_lento:.2f} % menos que el curso mas lento'
)
print(
    f'- Un {diff_rapido:.2f} % menos que la duracion promedio de los demas cursos'
)
print('--------------------')
# b)

# Duracion de crudos

crudo_promedio = 5
crudo_dalto = 3.5

tiempo_vacio_promedio = 100 - curso_promedio / crudo_promedio * 100
tiempo_vacio_dalto = 100 - este_curso / crudo_dalto * 100

print('--------------------')
print(
    f'''El curso de dalto tiene un crudo pormedio {tiempo_vacio_promedio}% menor al crudo promedio de los demas cursos'''
)
print(
    f'Este curso elimino el {tiempo_vacio_dalto:.2f}% de tiempo vacio'
)
print('--------------------')

# C)

# Mostrando diferencias si los cursos duraran 10 horas

print('--------------------')
print(
    f'Ver 10 horas de este curso equivale a ver {curso_promedio * 100 // este_curso / 10} horas de otros cursos')
print(
    f'Ver 10 horas de otros cursos equivale a ver {este_curso * 100 // curso_promedio / 10} horas de otros cursos')
print('--------------------')
