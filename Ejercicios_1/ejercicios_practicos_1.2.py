print('Hola, di una frase y calculare cuanto tardas en decirla')
frase = input().split()
len_frase = len(frase)
tiempo_frase = 2 * len(frase)


print(f'Tardarias en decir esa frase {tiempo_frase} segundos')
print(f'Dijiste {len_frase} palabras')

if tiempo_frase >= 60:
    print('Para flaco, tampoco te pedi un testamento')

tiempo_dalto = 30 * tiempo_frase / 100
frase_dalto = tiempo_frase - tiempo_dalto
print(f'Dalto tardaria {frase_dalto} segundos en decir la misma frase')
