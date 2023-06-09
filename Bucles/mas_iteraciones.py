frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]

cadena = "Hola Dalto"
numeros = [2, 5, 8, 10]

"""Continue"""

print()
print("------------------------------------------------")
print("Evitando que se coma una de las frutas con la sentencia continue")
print()

# realizamos el bucle
for fruta in frutas:
    # cuando el bucle llega o es igual a granada ejecuta el continue
    if fruta == "granada":
        # al colocar continue, cuando entre a este if ejecuta el continue y saltea todo lo de abajo y continua con la siguiente iteracion
        continue
    print(f"Me voy a comer una {fruta}")

"""Break"""

# cuando encuentra un break tampoco ejecuta el else del for

print("------------------------------------------------")
print("Evitando que el bucle siga ejecutandose, sentencia break")
print()

for fruta in frutas:
    if fruta == "pera":
        break  # con break el bucle se corta y no sigue iterando
    print(f"Me voy a comer una {fruta}")

print("------------------------------------------------")
print("Recorriendo una cadena de texto")
print()

"""Recorrer o iterar una cadena de texto"""

for letra in cadena:
    print(letra)

"""Bucle for en una sola linea de codigo, como yo lo conocia Comprension de listas"""

# x significa que cada elemento de la lista numeros va a ser multiplicado por 2
print("------------------------------------------------")
print("Comprension de listas")

numero_duplicados = [x * 2 for x in numeros]
print(numero_duplicados)
