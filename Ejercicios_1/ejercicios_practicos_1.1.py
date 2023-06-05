# Para resolver el ejercicio, lo primero que tenemos que hacer es anotar los datos

# a)

# Duracion de cursos
este_curso = float(1.5)
curso_minimo = float(2.5)
curso_promedio = float(4)
curso_maximo = float(7)

diff_rapido = 100 - este_curso / curso_minimo * 100
diff_lento = 100 - este_curso / curso_maximo * 100
diff_promedio = 100 - este_curso / curso_promedio * 100

print(
    f'El curso de dalto dura {diff_rapido:.2f} % menos que el curso mas rapido'
)
print(
    f'El curso de dalto dura {diff_lento:.2f} % menos que el curso mas lento'
)
print(
    f'El curso de dalto dura {diff_rapido:.2f} % menos que la duracion promedio de los demas cursos'
)

# b)

# Duracion de crudos

crudo_promedio = 5
crudo_dalto = 3.5

tiempo_vacio_promedio = 100 -
